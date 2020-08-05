from flask import Flask, flash, render_template, request, redirect, url_for, session
from fantasybasketball import app, mysql
from fantasybasketball.authentication import SignUpForm, SignInForm
import MySQLdb.cursors
from fantasybasketball.advanced_function import simulation,checkingToDropVariables,machineLearning
import pandas as pd
import itertools
import numpy as np
from patsy import dmatrices
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant
from sklearn.linear_model import LinearRegression
import csv

loggedin = False


@app.route('/crud', methods=['GET', 'POST'])
def crud():
    cur = mysql.connection.cursor()
    cur.execute("SELECT P.PlayerID, P.PlayerName, P.TeamName, P.Positions, P.Height, P.Weight, S.Points, S.Assists, S.Rebounds FROM Players P NATURAL JOIN Statistics S")
    output = cur.fetchall()
    if request.method == 'POST':
        if request.form['submit'] == 'add':
            a = request.form["Player_Add"]
            b= request.form["Name_Add"]
            z = request.form["TeamName_Add"]
            c =  request.form["Position_Add"]
            d=  request.form["Height_Add"]
            e= request.form["Weight_Add"]
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO Players Values(%s, %s, %s, %s, %s, %s)",(a,b,z,c,d,e))
            mysql.connection.commit()
            cur.close()
        elif request.form['submit'] == 'delete':
            a = request.form["PlayerId_Delete"]
            cur = mysql.connection.cursor()
            cur.execute("DELETE FROM Players WHERE PlayerId = %s",(a,))
            mysql.connection.commit()
            cur.close()
        elif request.form['submit'] == 'update':
            a = request.form["PlayerId_Update"]
            b = request.form["Height_Update"]
            c = request.form["Weight_Update"]
            cur = mysql.connection.cursor()
            cur.execute("UPDATE Players SET Height=%s,Weight=%s WHERE PlayerId =%s",(b,c,a))
            mysql.connection.commit()
            cur.close()
        elif request.form['submit'] == 'model':
            print("hello")
            checkingToDropVariables()
            # machineLearning()
        if request.form['submit'] == 'search':
            cur = mysql.connection.cursor()
            a = request.form["Name_Search"]
            b = request.form["Team_Search"]
            c = request.form["Position_Search"]
            d = request.form["Min_Height_Search"]
            e = request.form["Max_Height_Search"]
            f = request.form["Min_Weight_Search"]
            g = request.form["Max_Weight_Search"]

            query = "SELECT P.PlayerID, P.PlayerName, P.TeamName, P.Positions, P.Height, P.Weight, S.Points, S.Assists, S.Rebounds FROM Players P NATURAL JOIN Statistics S WHERE PlayerName LIKE '%" + str(a) + "%'"
            if b:
                query = "SELECT P.PlayerID, P.PlayerName, P.TeamName, P.Positions, P.Height, P.Weight, S.Points, S.Assists, S.Rebounds, T.Wins, T.Loss FROM Players P NATURAL JOIN Statistics S JOIN Teams T ON (P.TeamName = T.TeamName) WHERE P.TeamName = '" + str(b) + "'"
            if a and b:
                query = "SELECT P.PlayerID, P.PlayerName, P.TeamName, P.Positions, P.Height, P.Weight, S.Points, S.Assists, S.Rebounds, T.Wins, T.Loss FROM Players P NATURAL JOIN Statistics S JOIN Teams T ON (P.TeamName = T.TeamName) WHERE PlayerName LIKE '%" + str(a) + "%'" + "AND Players.TeamName = '" + str(b) + "'"

            if c and (a or b):
                query += " AND Positions = '" + str(c) + "'"
            elif c:
                query = "SELECT P.PlayerID, P.PlayerName, P.TeamName, P.Positions, P.Height, P.Weight, S.Points, S.Assists, S.Rebounds FROM Players P NATURAL JOIN Statistics S WHERE Positions = '" + str(c) + "'"

            if d and (a or b or c):
                query += " AND Height >= " + d
            elif d:
                query = "SELECT P.PlayerID, P.PlayerName, P.TeamName, P.Positions, P.Height, P.Weight, S.Points, S.Assists, S.Rebounds FROM Players P NATURAL JOIN Statistics S WHERE Height >= " + d

            if e and (a or b or c or d):
                query += " AND Height <= " + e
            elif e:
                query = "SELECT P.PlayerID, P.PlayerName, P.TeamName, P.Positions, P.Height, P.Weight, S.Points, S.Assists, S.Rebounds FROM Players P NATURAL JOIN Statistics S WHERE Height <= " + e

            if f and (a or b or c or d or e):
                query += " AND Weight >= " + f
            elif f:
                query = "SELECT P.PlayerID, P.PlayerName, P.TeamName, P.Positions, P.Height, P.Weight, S.Points, S.Assists, S.Rebounds FROM Players P NATURAL JOIN Statistics S WHERE Weight >= " + f

            if g and (a or b or c or d or e or f):
                query += " AND Height <= " + g
            elif g:
                query = "SELECT P.PlayerID, P.PlayerName, P.TeamName, P.Positions, P.Height, P.Weight, S.Points, S.Assists, S.Rebounds FROM Players P NATURAL JOIN Statistics S WHERE Height <= " + g

            query += " ORDER BY Points DESC, Assists DESC, Rebounds DESC"
            cur.execute(query)
            output = cur.fetchall()
        # cur.close()
    #cur = mysql.connection.cursor()
    #cur.execute("SELECT * FROM Players")
    #output = cur.fetchall()
    # cur.close()

    return render_template("crud.html", output = output)

@app.route('/', methods=['GET', 'POST'])
def start():
    return redirect('/about')

@app.route('/about', methods=['GET', 'POST'])
def displayabout():
    return render_template('about.html')

@app.route('/home', methods=['GET', 'POST'])
def displayhome():


    # Change later to display specific scout's team's information
    global loggedin
    if loggedin:
        arrPlayerIds = []
        sim_arr = [[0,"",0.0,0.0,0.0],[0,"",0.0,0.0,0.0],[0,"",0.0,0.0,0.0]]
        stat_cur = mysql.connection.cursor()
        stat_cur.execute('''SELECT AVG(S.Points) AS Points, AVG(S.Assists) AS Assists, AVG(S.Rebounds) AS Rebounds
                        FROM Scouts Sc JOIN Teams T ON (Sc.Team = T.TeamName)
                        JOIN Players P ON (P.TeamName = T.TeamName)
                        JOIN Statistics S ON (P.PlayerID = S.PlayerID)
                        GROUP BY T.TeamName''')
        stats = stat_cur.fetchall()
        stats_cur = []
        for row in stats:
            stats_cur.append(round(float(row[0]),2))
            stats_cur.append(round(float(row[1]),2))
            stats_cur.append(round(float(row[2]),2))
        if request.method == 'POST':
            arrPlayerIds.clear()
            for x in range(1,26):
                place = ""
                place = "r" + str(x) + "c1"
                arrPlayerIds.append(request.form[place])
            temp = []
            for id in arrPlayerIds:
                if id != '0':
                    temp.append(id)
            arrPlayerIds = temp
            model = ""
            if request.form['submit'] == 'KCross':
                model = "KCross"
            elif request.form['submit'] == 'VIF':
                model = "VIF"
            sim = simulation(model, arrPlayerIds)
            sim_arr = [list(x) for x in sim]
            strPlayerIds = [str(x) for x in arrPlayerIds]
            currentPlayerIdsStr = ""
            currentPlayerIdsStr = ','.join(strPlayerIds)
            new_stat_cur = mysql.connection.cursor()
            new_stat_query = "SELECT AVG(S.Points) AS Points, AVG(S.Assists) AS Assists, AVG(S.Rebounds) AS Rebounds FROM Players P NATURAL JOIN Statistics S WHERE P.PlayerID IN (" + currentPlayerIdsStr + ")"
            new_stat_cur.execute(new_stat_query)
            result_new_stat = new_stat_cur.fetchall()
            print(result_new_stat)
            stats_cur = result_new_stat[0]



        print(sim_arr)
        # Team Roster
        ros_cur = mysql.connection.cursor()
        ros_cur.execute('''SELECT DISTINCT(P.PlayerID), P.PlayerName, S.Points,S.Assists,S.Rebounds
                        FROM Scouts Sc
                        JOIN Teams T ON (Sc.Team = T.TeamName)
                        JOIN Players P ON (T.TeamName = P.TeamName)
                        JOIN Statistics S ON (P.PlayerID = S.PlayerID)
                        ORDER BY Points DESC, Assists DESC, Rebounds DESC''')
        players = ros_cur.fetchall()
        players_holder = []
        lengthPlayers = len(players)

        for row in players:
            players_holder.append([int(row[0]), str(row[1]), float(row[2]),float(row[3]),float(row[4])])
        fillLength = 25 - len(players)
        for x in range(fillLength):
            players_holder.append([0,"Insert Name",0.0, 0.0, 0.0])

        # Team Statistics
        #Check to see


        # Recommendations
        # Check to see if button from front end has been clicked to run simulation(machine learning algo) here
        # rec_return = simulation()
        # rec_cur = []
        # for row in rec_return:
        #     rec_cur.append([int(row[0]), str(row[1]), int(row[2]), int(row[3]), int(row[4])]) rec_play=rec_cur

        #Check to see if button has been clicked to run new model
        # if button has been clicked
        #   checkingToDropVariables()
        #   machineLearning()

        # Decide which model user selects
        # print("Outside Function")
        # model = "VIF"
        # if request.method == 'POST':
        #     print("Came Function")
        #     if request.form['submit_button'] == 'KCross':
        #         print("KCross")
        #         model = "KCross"
        #         simulation(model, arrPlayerIds)
        #     elif request.form['submit_button'] == 'VIF':
        #         print("VIF")
        #         model = "VIF"
        #         simulation(model, arrPlayerIds)

        return render_template('home.html', user_players=players_holder, team_stats=stats_cur,sim_players = sim_arr)
    else:
        return "<h1> Log in to see your user data. </h1>"

@app.route('/signin',methods=['GET', 'POST'])
def signin():
    global loggedin
    if loggedin:
        return "You are already signed in as " + session['username'] + "."
    user_form = SignInForm()
    if request.method == 'POST':
        if user_form.validate_on_submit():
            # check if the data submitted by the user is correct
            cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute('''SELECT * FROM Scouts WHERE Username = %s AND Password = %s AND Email = %s''', (user_form.username.data, user_form.password.data, user_form.email.data,))
            user = cur.fetchone()
            if user:
                loggedin = True
                session['loggedin'] = True
                session['username'] = user['Username']
                session['password'] = user['Password']
                session['email'] = user['Email']
                # Login User and display their information
                return redirect('/home')
            else:
                return "<h1> You have entered an incorrect email, username, and password combination. Please restart sign in. </h1>"
        return render_template('signin.html', form=user_form)
    return render_template('signin.html', form=user_form)

@app.route('/signout',methods=['GET', 'POST'])
def signout():
    # Logout User
    global loggedin
    loggedin = False
    session.pop('loggedin', None)
    session.pop('username', None)
    session.pop('password', None)
    return redirect('/about')

@app.route('/signup',methods=['GET', 'POST'])
def signup():
    user_form = SignUpForm()
    if request.method == 'POST':
        if user_form.validate_on_submit() and valid_team(user_form.team.data):
            # Insert the new scout's attributes into database
            cur = mysql.connection.cursor()
            cur.execute("""INSERT INTO Scouts VALUES (%s, %s, %s, %s)""", (user_form.email.data, user_form.username.data, user_form.password.data, user_form.team.data))
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('signin'))
        else:
            # account has invalid team or invalid input
            return "<h1> Team does not exist. Please restart sign up. </h1>"
    return render_template('signup.html', form=user_form)

def valid_team(team):
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('''SELECT * FROM Teams WHERE TeamName = %s''', (team,))
    t = cur.fetchone()
    if t:
        return True
    return False
