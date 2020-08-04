from flask import Flask, flash, render_template, request, redirect, url_for, session
from fantasybasketball import app, mysql
from fantasybasketball.authentication import SignUpForm, SignInForm
import MySQLdb.cursors
from fantasybasketball.advanced_function import simulation
import pandas as pd
import itertools
import numpy as np
from patsy import dmatrices
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant
from sklearn.linear_model import LinearRegression
import csv

loggedin = False

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
        # Team Roster
        ros_cur = mysql.connection.cursor()
        ros_cur.execute('''SELECT P.PlayerID, P.PlayerName, S.Points, S.Assists, S.Rebounds
                        FROM Scouts Sc
                        JOIN Teams T ON (Sc.Team = T.TeamName)
                        JOIN Players P ON (T.TeamName = P.TeamName)
                        JOIN Statistics S ON (P.PlayerID = S.PlayerID)
                        ORDER BY Points DESC, Assists DESC, Rebounds DESC''')
        players = ros_cur.fetchall()
        players_holder = []

        #filter out excess ids
        id_checker = {}

        for row in players:
            if int(row[0]) not in id_checker:
                players_holder.append([int(row[0]), str(row[1]), float(row[2]), float(row[3]), float(row[4])])
            id_checker[row[0]] = 1

        # Team Statistics
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

        # Recommendations
        # rec_return = simulation()
        rec_cur = []
        # for row in rec_return:
            # rec_cur.append([int(row[0]), str(row[1]), int(row[2]), int(row[3]), int(row[4])])
        return render_template('home.html', user_players=players_holder, team_stats=stats_cur, rec_play=rec_cur)
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
