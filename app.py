from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import pandas as pd
import itertools


app = Flask(__name__,template_folder='templates')
app.config['MYSQL_USER'] = 'sql3356970'
app.config['MYSQL_PASSWORD'] = 'gAgxITG1pb'
app.config['MYSQL_HOST'] = 'sql3.freemysqlhosting.net'
app.config['MYSQL_DB'] = 'sql3356970'
app.config['MYSQL_CURSURCLASS'] = 'DictCursor'

mysql = MySQL(app)
table1 = ""



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
    return render_template('advanced.html',output_one=rows,output_two=row_two)
if __name__ == 'main':
    app.run(debug=True)

@app.route('/cor')
def correlation_matrix():
    cur = mysql.connection.cursor()
    qu = 'SELECT AVG(S.FieldGoalAttempts), AVG(S.FieldGoalPercent), AVG(S.ThreePointAttempts), AVG(S.ThreePointPercent), AVG(S.TwoPointAttempts), AVG(S.TwoPointPercent), AVG(S.EFieldGoal), AVG(S.FreeThrowAttempts), AVG(S.FreeThrowPercent), AVG(S.Rebounds), AVG(S.Assists), AVG(S.Steals), AVG(S.Blocks), AVG(S.Turnovers), AVG(S.PersonalFouls), AVG(S.Points), COUNT(*) FROM Teams T NATURAL JOIN Players P JOIN Statistics S ON (P.PlayerID = S.PlayerID) WHERE T.NumGames = 82 GROUP BY T.TeamName'
    output = cur.execute(qu)
    records = cur.fetchall()
    teamStats = {}
    for row in records:
        teamStats["FieldGoalAttempts"]= [row[0]]
        teamStats["FieldGoalPercent"] = [row[1]]
    for k,v in teamStats.items():
        print (k,v)
    
    return


