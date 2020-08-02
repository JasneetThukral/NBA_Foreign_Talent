from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import pandas as pd
import itertools
import numpy as np
from patsy import dmatrices
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant
from sklearn.linear_model import LinearRegression


app = Flask(__name__,template_folder='templates')
app.config['MYSQL_USER'] = 'sql3356970'
app.config['MYSQL_PASSWORD'] = 'gAgxITG1pb'
app.config['MYSQL_HOST'] = 'sql3.freemysqlhosting.net'
app.config['MYSQL_DB'] = 'sql3356970'
app.config['MYSQL_CURSURCLASS'] = 'DictCursor'

mysql = MySQL(app)
table1 = ""
verifyAttributes = []



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        query = details['statement']
        print(details)
        global table1
        table1 = details['table']
        cur = mysql.connection.cursor()
        row = cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print(row)
        mysql.connection.commit()
        cur.close()
    return render_template('index.html')

@app.route('/scout_home',methods=['GET', 'POST'])
def scout_login():
    return "<h1> Scout Login </h1>"

@app.route('/commissioner_home',methods=['GET', 'POST'])
def commissioner_login():
    return "<h1> Commissioner Login </h1>"

@app.route('/results',methods=['GET', 'POST'])
def script_output():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM " + str(table1))
    rows = cur.fetchall()
    print(rows)
    cur.close()
    return render_template('results.html',output=rows,table=table1)

@app.route('/advanced',methods=['GET', 'POST'])
def advance():
    cur = mysql.connection.cursor()
    cur_two = mysql.connection.cursor()
    # if str(table) == "Players":
    output_one = cur.execute("Select count(p.PlayerID), t.wins From Players p, Teams t Where p.TeamName = t.TeamName AND p.height > 78 Group by t.TeamName")
    output_two = cur_two.execute("Select count(p.PlayerID), t.wins From Players p, Teams t Where p.TeamName = t.TeamName AND p.weight > 200 Group by t.TeamName")
    rows = cur.fetchall()
    row_two = cur_two.fetchall()
    print(rows)
    cur.close()
    cur_two.close()
    return render_template('advanced.html',output_one=rows,output_two=row_two)
if __name__ == 'main':
    app.run(debug=True)

@app.route('/drop')
def checkingToDropVariables():
    cur = mysql.connection.cursor()
    qu = 'SELECT AVG(S.FieldGoalAttempts), AVG(S.FieldGoalPercent), AVG(S.ThreePointAttempts), AVG(S.ThreePointPercent), AVG(S.TwoPointAttempts), AVG(S.TwoPointPercent), AVG(S.EFieldGoal), AVG(S.FreeThrowAttempts), AVG(S.FreeThrowPercent), AVG(S.Rebounds), AVG(S.Assists), AVG(S.Steals), AVG(S.Blocks), AVG(S.Turnovers), AVG(S.PersonalFouls), AVG(S.Points) FROM Teams T NATURAL JOIN Players P JOIN Statistics S ON (P.PlayerID = S.PlayerID) WHERE T.NumGames = 82 GROUP BY T.TeamName'
    output = cur.execute(qu)
    records = cur.fetchall()
    teamStats = {"FieldGoalAttempts": [], "FieldGoalPercent": [], "ThreePointAttempts": [], "ThreePointPercent": [], "TwoPointAttempts": [],
                "TwoPointPercent": [],"EFieldGoal": [],"FreeThrowAttempts": [],"FreeThrowPercent": [], "Rebounds": [],"Assists": [],
                "Steals": [],"Blocks": [], "Turnovers": [],"PersonalFouls": [], "Points": [] }
                
    for row in records:
        teamStats["FieldGoalAttempts"].append(row[0])
        teamStats["FieldGoalPercent"].append(row[1])
        teamStats["ThreePointAttempts"].append(row[2])
        teamStats["ThreePointPercent"].append(row[3])
        teamStats["TwoPointAttempts"].append(row[4])
        teamStats["TwoPointPercent"].append(row[5])
        teamStats["EFieldGoal"].append(row[6])
        teamStats["FreeThrowAttempts"].append(row[7])
        teamStats["FreeThrowPercent"].append(row[8])
        teamStats["Rebounds"].append(row[9])
        teamStats["Assists"].append(row[10])
        teamStats["Steals"].append(row[11])
        teamStats["Blocks"].append(row[12])
        teamStats["Turnovers"].append(row[13])
        teamStats["PersonalFouls"].append(row[14])
        teamStats["Points"].append(row[15])

    dataF = pd.DataFrame(teamStats, columns = ["FieldGoalAttempts", "FieldGoalPercent", "ThreePointAttempts", "ThreePointPercent", "TwoPointAttempts",
                "TwoPointPercent","EFieldGoal","FreeThrowAttempts","FreeThrowPercent", "Rebounds","Assists",
                "Steals","Blocks", "Turnovers","PersonalFouls", "Points"])
    
    fields = list(dataF.columns)
    correlationMatrix = dataF.corr()
    rows,cols = correlationMatrix.shape
    global verifyAttributes

    #Figure out which variables are under the suspicion of mulitcollinearity using correlation matrix
    for i in range(cols):
        for j in range(i, cols):
            if ((correlationMatrix[fields[i]][j] > 0.7 and correlationMatrix[fields[i]][j] < 1.0)
                or (correlationMatrix[fields[i]][j] < -0.7 and correlationMatrix[fields[i]][j] > -1.0)):
                verifyAttributes.append([fields[i], fields[j]])

    # Getting rid of duplicates from verifyAttributes
    temp = []
    for elem in verifyAttributes:
        if elem not in temp:
            temp.append(elem)
    verifyAttributes = temp
    cur.close()

    # Calculate which attributes have a high vif value
    vifDrops = []
    if (len(verifyAttributes) > 0):
        while True:
            X = add_constant(dataF)
            vif = pd.Series([variance_inflation_factor(X.values, i) 
               for i in range(X.shape[1])], 
                index=X.columns)
            vif.drop('const', axis = 0, inplace=True)
            if (vif.max() > 5):
                theMax = vif.idxmax()
                vifDrops.append([theMax, vif.max()])
                dataF.drop(theMax, axis=1, inplace=True)
            else:
                break

    print("VIF will drop these variables: ", vifDrops)
    #Running the r-Values Function here as it does not have a path
    #r_values()
    return

"""
def r_values():
    data = pd.read_csv('NBARankings.csv')
    rankings = data['rankings'].values
    matrix = []
    allAtributes = ["FieldGoalAttempts", "FieldGoalPercent", "ThreePointAttempts", "ThreePointPercent", "TwoPointAttempts",
                "TwoPointPercent","EFieldGoal","FreeThrowAttempts","FreeThrowPercent", "Rebounds","Assists",
                "Steals","Blocks", "Turnovers","PersonalFouls", "Points"]
    for elem in verifyAttributes:
        # CSV File matches with the results of this query based on alphabetical order *HARDCODED*
        cur = mysql.connection.cursor()
        output_one = cur.execute("SELECT AVG(S.%s) FROM Teams T NATURAL JOIN Players P JOIN Statistics S ON (P.PlayerID = S.PlayerID) WHERE T.NumGames = 82 GROUP BY T.TeamName ORDER BY T.TeamName" %elem[0])
        results_one = cur.fetchall()

        firstXValues = [x for [x] in results_one]
        firstCorrMatrix = np.corrcoef(firstXValues, rankings)
        firstRValue = firstCorrMatrix[0,1]
        print(elem[0], firstRValue)

        cur2 = mysql.connection.cursor()
        output_two = cur2.execute("SELECT AVG(S.%s) FROM Teams T NATURAL JOIN Players P JOIN Statistics S ON (P.PlayerID = S.PlayerID) WHERE T.NumGames = 82 GROUP BY T.TeamName ORDER BY T.TeamName" %elem[1])
        results_two = cur2.fetchall()

        secondXValues = [x for [x] in results_two]
        secondCorrMatrix = np.corrcoef(secondXValues, rankings)
        secondRValue = secondCorrMatrix[0,1]
        print(elem[1], secondRValue)
    return
"""

@app.route('/kCross')
def machineLearning():
    #Find all the combinations of different lengths of all attributes to create various models to insert into k-cross
    allAtributes = ["FieldGoalAttempts", "FieldGoalPercent", "ThreePointAttempts", "ThreePointPercent", "TwoPointAttempts",
                "TwoPointPercent","EFieldGoal","FreeThrowAttempts","FreeThrowPercent", "Rebounds","Assists",
                "Steals","Blocks", "Turnovers","PersonalFouls", "Points"]
    allCombinations = []
    cur = mysql.connection.cursor()
    qu = 'SELECT AVG(S.FieldGoalAttempts), AVG(S.FieldGoalPercent), AVG(S.ThreePointAttempts), AVG(S.ThreePointPercent), AVG(S.TwoPointAttempts), AVG(S.TwoPointPercent), AVG(S.EFieldGoal), AVG(S.FreeThrowAttempts), AVG(S.FreeThrowPercent), AVG(S.Rebounds), AVG(S.Assists), AVG(S.Steals), AVG(S.Blocks), AVG(S.Turnovers), AVG(S.PersonalFouls), AVG(S.Points) FROM Teams T NATURAL JOIN Players P JOIN Statistics S ON (P.PlayerID = S.PlayerID) WHERE T.NumGames = 82 GROUP BY T.TeamName'
    output = cur.execute(qu)
    records = cur.fetchall()
    teamStats = {"FieldGoalAttempts": [], "FieldGoalPercent": [], "ThreePointAttempts": [], "ThreePointPercent": [], "TwoPointAttempts": [],
                "TwoPointPercent": [],"EFieldGoal": [],"FreeThrowAttempts": [],"FreeThrowPercent": [], "Rebounds": [],"Assists": [],
                "Steals": [],"Blocks": [], "Turnovers": [],"PersonalFouls": [], "Points": [] }
                
    for row in records:
        teamStats["FieldGoalAttempts"].append(row[0])
        teamStats["FieldGoalPercent"].append(row[1])
        teamStats["ThreePointAttempts"].append(row[2])
        teamStats["ThreePointPercent"].append(row[3])
        teamStats["TwoPointAttempts"].append(row[4])
        teamStats["TwoPointPercent"].append(row[5])
        teamStats["EFieldGoal"].append(row[6])
        teamStats["FreeThrowAttempts"].append(row[7])
        teamStats["FreeThrowPercent"].append(row[8])
        teamStats["Rebounds"].append(row[9])
        teamStats["Assists"].append(row[10])
        teamStats["Steals"].append(row[11])
        teamStats["Blocks"].append(row[12])
        teamStats["Turnovers"].append(row[13])
        teamStats["PersonalFouls"].append(row[14])
        teamStats["Points"].append(row[15])
    data = pd.read_csv('NBARankings.csv')
    y = data['rankings'].values
    y = np.array(y)

    for x in range(1, len(allAtributes) + 1):
        allCombinations.append(list(itertools.combinations(allAtributes, x)))
    for elem in allCombinations:#((3PA, PF,P),(3PA, PF, 2PA))
        for combination in elem: #(3Pa, PF, P)
            dataset = []
            for attribute in combination: #3PA
                dataset.append(teamStats[attribute])
            dataset = np.array(dataset)
            #LinearRegression().fit(np.transpose(dataset), np.transpose(y))
            for attr in dataset:
                print(dataset[attr])
    
        
"""
    Find all different combinations of the attributes' values
    For every combination:
        All splits = [Use K cross to split the data]
        For every split:
            Create linear regression line using the train data with rankings as dependent variable 
            Use linear regression line to predict test data
            Compute the square of error
        Compute the sum of squared errors
        Find the 
    
    
"""
    



    