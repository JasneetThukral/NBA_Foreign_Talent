from flask import Flask, flash, render_template, request, redirect, url_for, session
from fantasybasketball import app, mysql
from fantasybasketball.authentication import SignUpForm, SignInForm
import MySQLdb.cursors

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
        render_template('home.html', login=True)
    else:
        render_template('home.html', login=False)

@app.route('/favorites', methods=['GET', 'POST'])
def displayfavorites():
    return ""

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
