from flask import Flask, render_template, request
import pandas as pd
import itertools
import numpy as np
from patsy import dmatrices
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant
from sklearn.linear_model import LinearRegression
import csv
from fantasybasketball import app, mysql

def simulation():
    #TODO: Front End: Give all of the player IDs that exists in team roster when the user clicks delete
        #This is hardcoded right now below for testing purposes --> These are 3 player Ids (first 2 from NBA Team (GSW), last one from Euro or Greek League(AEKAthens))
    currentPlayerIds = [625, 639, 116]

    # #TODO: Front End: check to see if toggle button is either vif
    # attr_values = pd.read_csv("vif_model.csv")
    # data = pd.read_csv("NBARankings.csv")
    # rankings = data["rankings"].values
    # rankings = np.array(rankings)

    # #build vif model using csv file and sklearn
    # x_values = attr_values.values.tolist()
    # x_values = np.array(x_values)

    # vif_lr = LinearRegression().fit(x_values, np.transpose(rankings))

    # #Add attributes to an array and modify for proper syntax to send to query
    # headers = []
    # queryAttrArr = []
    # queryAttr = ""
    # for col_name in attr_values.columns:
    #     headers.append(col_name)
    # for header in headers:
    #     header = "S." + header + ", "
    #     queryAttrArr.append(header)
    # queryAttrArr[len(queryAttrArr) - 1] = queryAttrArr[len(queryAttrArr) - 1].replace(",", '')
    # queryAttr = queryAttr.join(queryAttrArr)

    # # Write query to get the average stats of the attributes from queryAttr from
    # cur = mysql.connection.cursor()
    # #TODO: Figure out if the IDs from Front end is coming in as a string or as an array of numbers.
    # #      If it is an array leave the next 2 lines, otherwise delete the next 2 lines.
    # strPlayerIds = [str(x) for x in currentPlayerIds]
    # currentPlayerIdsStr = ""
    # currentPlayerIdsStr = ','.join(strPlayerIds)
    # currentPlayersQuery = "SELECT " + queryAttr + "FROM Statistics S NATURAL JOIN Players P WHERE P.PlayerID IN (" + currentPlayerIdsStr + ")"
    # output = cur.execute(currentPlayersQuery)
    # valuesOfCurrentTeam = cur.fetchall()

    # # average each element
    # arr = [list(x) for x in valuesOfCurrentTeam]
    # numPlayers = (len(arr))
    # npArr = np.array(arr)
    # npArr = np.mean(npArr, axis=0)
    # averageCurrentPlayersStats = npArr.tolist()

    # #Find all of the playerIDs that I can predict --> No NBA Players, no current player ids
    # cur_2 = mysql.connection.cursor()
    # possiblePlayersQuery = "SELECT P.PlayerID FROM Players P NATURAL JOIN Teams T WHERE P.PlayerID NOT IN(" + currentPlayerIdsStr + ") AND T.NumGames NOT IN (82)"
    # output_two = cur_2.execute(possiblePlayersQuery)
    # possiblePlayers = cur_2.fetchall()
    # possiblePlayersId = [x[0] for x in possiblePlayers]

    # #loop through all of the player IDs, add into listNpArr, average again, send to predict function, get the highest ranking
    # predictedRankings = []
    # for eachId in possiblePlayersId:
    #     cur_3 = mysql.connection.cursor()
    #     predictPlayerStatsQuery = "SELECT " + queryAttr + "FROM Statistics S NATURAL JOIN Players P WHERE P.PlayerID IN (" + str(eachId) + ")"
    #     output_three = cur_3.execute(predictPlayerStatsQuery)
    #     thisPlayer = cur_3.fetchall()
    #     newPlayerStats = list(thisPlayer[0])

    #     #calculate new average
    #     newTeamAverage = []
    #     for x in range(len(averageCurrentPlayersStats)):
    #         newAverage = ((averageCurrentPlayersStats[x] * numPlayers) + newPlayerStats[x])/(numPlayers + 1)
    #         newTeamAverage.append(newAverage)
    #     newTeamAverage = np.array(newTeamAverage)
    #     ranking = vif_lr.predict(np.transpose(newTeamAverage).reshape(1,-1))
    #     predictedRankings.append([list(ranking), eachId])
    # predictedRankings = sorted(predictedRankings, key=lambda x: x[0], reverse=False)
    # firstThree = []
    # firstThree.append(predictedRankings[0][1])
    # firstThree.append(predictedRankings[1][1])
    # firstThree.append(predictedRankings[2][1])

    # firstThreeStrConvert = [str(x) for x in firstThree]
    # firstThreeStr = ""
    # firstThreeStr = ",".join(firstThreeStrConvert)
    # cur_4 = mysql.connection.cursor()
    # top3PlayersQuery = "SELECT P.PlayerId, P.PlayerName, P.TeamName FROM Players P WHERE P.PlayerID IN (" + firstThreeStr + ")"
    # output_four = cur_4.execute(top3PlayersQuery)
    # top3Players = cur_4.fetchall()
    # print(top3Players)
    # #TODO:Figure out how to format the top 3 information to give back to front end (prob will pass these values in when I renderTemplate)


    #TODO:check to see if toggle button is either k_cross
    # Create helper function the parameter should be which attributes to use for simulations
    attr_values = pd.read_csv("kcross_model.csv")
    data = pd.read_csv("NBARankings.csv")
    rankings = data["rankings"].values
    rankings = np.array(rankings)

    #build vif model using csv file and sklearn
    x_values = attr_values.values.tolist()
    x_values = np.array(x_values)

    vif_lr = LinearRegression().fit(x_values, np.transpose(rankings))

    #Add attributes to an array and modify for proper syntax to send to query
    headers = []
    queryAttrArr = []
    queryAttr = ""
    for col_name in attr_values.columns:
        headers.append(col_name)
    for header in headers:
        header = "S." + header + ", "
        queryAttrArr.append(header)
    queryAttrArr[len(queryAttrArr) - 1] = queryAttrArr[len(queryAttrArr) - 1].replace(",", '')
    queryAttr = queryAttr.join(queryAttrArr)

    # Write query to get the average stats of the attributes from queryAttr from
    cur = mysql.connection.cursor()
    #TODO: Figure out if the IDs from Front end is coming in as a string or as an array of numbers.
    #      If it is an array leave the next 2 lines, otherwise delete the next 2 lines.
    strPlayerIds = [str(x) for x in currentPlayerIds]
    currentPlayerIdsStr = ""
    currentPlayerIdsStr = ','.join(strPlayerIds)
    currentPlayersQuery = "SELECT " + queryAttr + "FROM Statistics S NATURAL JOIN Players P WHERE P.PlayerID IN (" + currentPlayerIdsStr + ")"
    output = cur.execute(currentPlayersQuery)
    valuesOfCurrentTeam = cur.fetchall()

    # average each element
    arr = [list(x) for x in valuesOfCurrentTeam]
    numPlayers = (len(arr))
    npArr = np.array(arr)
    npArr = np.mean(npArr, axis=0)
    averageCurrentPlayersStats = npArr.tolist()

    #Find all of the playerIDs that I can predict --> No NBA Players, no current player ids
    cur_2 = mysql.connection.cursor()
    possiblePlayersQuery = "SELECT P.PlayerID FROM Players P NATURAL JOIN Teams T WHERE P.PlayerID NOT IN(" + currentPlayerIdsStr + ") AND T.NumGames NOT IN (82)"
    output_two = cur_2.execute(possiblePlayersQuery)
    possiblePlayers = cur_2.fetchall()
    possiblePlayersId = [x[0] for x in possiblePlayers]

    #loop through all of the player IDs, add into listNpArr, average again, send to predict function, get the highest ranking
    predictedRankings = []
    for eachId in possiblePlayersId:
        cur_3 = mysql.connection.cursor()
        predictPlayerStatsQuery = "SELECT " + queryAttr + "FROM Statistics S NATURAL JOIN Players P WHERE P.PlayerID IN (" + str(eachId) + ")"
        output_three = cur_3.execute(predictPlayerStatsQuery)
        thisPlayer = cur_3.fetchall()
        newPlayerStats = list(thisPlayer[0])

        #calculate new average
        newTeamAverage = []
        for x in range(len(averageCurrentPlayersStats)):
            newAverage = ((averageCurrentPlayersStats[x] * numPlayers) + newPlayerStats[x])/(numPlayers + 1)
            newTeamAverage.append(newAverage)
        newTeamAverage = np.array(newTeamAverage)
        ranking = vif_lr.predict(np.transpose(newTeamAverage).reshape(1,-1))
        predictedRankings.append([list(ranking), eachId])
    predictedRankings = sorted(predictedRankings, key=lambda x: x[0], reverse=False)
    firstThree = []
    firstThree.append(predictedRankings[0][1])
    firstThree.append(predictedRankings[1][1])
    firstThree.append(predictedRankings[2][1])

    firstThreeStrConvert = [str(x) for x in firstThree]
    firstThreeStr = ""
    firstThreeStr = ",".join(firstThreeStrConvert)
    cur_4 = mysql.connection.cursor()
    top3PlayersQuery = "SELECT P.PlayerId, P.PlayerName, S.Points, S.Assists, S.Rebounds FROM Players P NATURAL JOIN Statistics S WHERE P.PlayerID IN (" + firstThreeStr + ")"
    output_four = cur_4.execute(top3PlayersQuery)
    top3Players = cur_4.fetchall()
    print(top3Players)
    return top3Players
    # python list of top 3 players with

    #TODO:Figure out how to format the top 3 information to give back to front end (prob will pass these values in when I renderTemplate)
    # if Loggedin:
    #   return returnedtemplate
    # else:
    #   return <h1>"You must logged in to see your user data"<\h1>

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

    # Calculate which attributes have a high variance inflamation factor (VIF) value
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
                vifDrops.append(theMax)
                dataF.drop(theMax, axis=1, inplace=True)
            else:
                break

    #csv file processing and write model to csv
    for cur_drop in vifDrops:
        del teamStats[cur_drop]

    csv_labels = []
    csv_arr = []
    for i in teamStats:
        csv_arr.append(teamStats[i])
        csv_labels.append(i)

    csv_arr = np.array(csv_arr)
    csv_arr = np.transpose(csv_arr)

    with open('vif_model.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_arr)

    df = pd.read_csv("vif_model.csv", header=None)
    attr_values = df.to_csv("vif_model.csv", header=csv_labels, index=False)

    r_values()
    return

def r_values():
    data = pd.read_csv('NBARankings.csv')
    rankings = data['rankings'].values
    matrix = []
    allAtributes = ["FieldGoalAttempts", "FieldGoalPercent", "ThreePointAttempts", "ThreePointPercent", "TwoPointAttempts",
                "TwoPointPercent","EFieldGoal","FreeThrowAttempts","FreeThrowPercent", "Rebounds","Assists",
                "Steals","Blocks", "Turnovers","PersonalFouls", "Points"]

    for elem in verifyAttributes:
        # CSV File matches with the results of this query based on alphabetical order
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

def machineLearning():
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

    #populuate attributes with data from database
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

    #Find all the combinations of different lengths of all attributes to create various models to insert into k-cross-validation
    for x in range(1, len(allAtributes) + 1):
        allCombinations.append(list(itertools.combinations(allAtributes, x)))

    #create array that will store model and associated score
    # [([model 1], score1), ([model 2], score2), ([model 3], score3)]
    model_scores = []
    for elem in allCombinations:
        for combination in elem:

            x_vals_first_split_train = []  #10-30
            first_split_test = []  #0-10

            x_vals_second_split_train = [] #0-10 + 20-30
            second_split_test = []  #10-20

            x_vals_third_split_train = []  #0-20
            third_split_test = []  #20-30

            #extract data for all the combinations
            for attribute in combination:
                x_vals_first_split_train.append((teamStats[attribute])[10:30])
                first_split_test.append((teamStats[attribute])[0:10])

                temp_0_10 = teamStats[attribute][0:10]
                temp_20_30 = teamStats[attribute][10:20]
                temp_combined = []
                for i in range(10):
                    temp_combined.append(temp_0_10[i])
                for j in range(10):
                    temp_combined.append(temp_20_30[i])
                x_vals_second_split_train.append(temp_combined)
                second_split_test.append((teamStats[attribute])[10:20])

                x_vals_third_split_train.append((teamStats[attribute])[0:20])
                third_split_test.append((teamStats[attribute])[20:30])

            #make all y combinations
            y_1 = y[10:30]
            temp_1 = y[0:10]
            temp_2 = y[20:30]
            y_2 = np.concatenate((temp_1 , temp_2))
            y_3 = y[0:20]

            #make dataset compatable with numpy
            x_vals_first_split_train = np.array(x_vals_first_split_train)
            x_vals_second_split_train = np.array(x_vals_second_split_train)
            x_vals_third_split_train = np.array(x_vals_third_split_train)

            first_split_test = np.array(first_split_test)
            second_split_test = np.array(second_split_test)
            third_split_test = np.array(third_split_test)

            #make linear regression with train data
            lr_first_split_train = LinearRegression().fit(np.transpose(x_vals_first_split_train), np.transpose(y_1))
            lr_second_split_train = LinearRegression().fit(np.transpose(x_vals_second_split_train), np.transpose(y_2))
            lr_third_split_train = LinearRegression().fit(np.transpose(x_vals_third_split_train), np.transpose(y_3))

            sse_1 = 0
            #for every test point...
            for data_point_num in range(10):
                single_point = []
                for attrArr in first_split_test:
                    single_point_attribute = []
                    single_point_attribute.append(attrArr[data_point_num])
                    single_point.append(single_point_attribute)
                #once we have a point we want to predict, predict point
                single_point = np.array(single_point)
                # single_point = np.transpose(single_point)
                predicted_val = lr_first_split_train.predict(np.transpose(single_point))
                #find Squared Error of point and to sse
                actual_val = y[data_point_num] #0-10
                sse_1 += pow((actual_val - predicted_val), 2)

            #plot all predict points and find sse for second split
            sse_2 = 0
            for data_point_num in range(10):
                single_point = []
                for attrArr in second_split_test:
                    single_point_attribute = []
                    single_point_attribute.append(attrArr[data_point_num])
                    single_point.append(single_point_attribute)
                single_point = np.array(single_point)
                predicted_val = lr_second_split_train.predict(np.transpose(single_point))
                idx = 10 + data_point_num
                actual_val = y[idx] #10-20
                sse_2 += pow((actual_val - predicted_val), 2)

            #plot all predict points and find sse for third split
            sse_3 = 0
            for data_point_num in range(10):
                single_point = []
                for attrArr in third_split_test:
                    single_point_attribute = []
                    single_point_attribute.append(attrArr[data_point_num])
                    single_point.append(single_point_attribute)
                single_point = np.array(single_point)
                predicted_val = lr_third_split_train.predict(np.transpose(single_point))
                idx = 20 + data_point_num
                actual_val = y[idx] #20-30
                sse_3 += pow((actual_val - predicted_val), 2)

            avg_sse = (sse_1 + sse_2 + sse_3)/3
            model_scores.append([combination, avg_sse])

    #print at the end
    # [[[model 1], score1], [[model 2], score2], [[model 3], score3]]
    min = model_scores[0][1]
    min_arr = []
    myLen = len(model_scores)
    for cur_sse in range(myLen):
        if (model_scores[cur_sse][1] < min):
            min = model_scores[cur_sse][1]
            min_arr = model_scores[cur_sse][0]

    #csv file processing and write model to csv
    drop_arr = []
    for i in allAtributes:
        if (i not in min_arr):
            drop_arr.append(i)

    for cur_drop in drop_arr:
        del teamStats[cur_drop]

    csv_labels = []
    csv_arr = []
    for i in teamStats:
        csv_arr.append(teamStats[i])
        csv_labels.append(i)

    csv_arr = np.array(csv_arr)
    csv_arr = np.transpose(csv_arr)

    with open('kcross_model.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_arr)

    df = pd.read_csv("kcross_model.csv", header=None)
    attr_values = df.to_csv("kcross_model.csv", header=csv_labels, index=False)

    return
