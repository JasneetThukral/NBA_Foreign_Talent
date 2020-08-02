from flask import Flask, flash, render_template, request, redirect, url_for
from fantasybasketball import app, mysql
from flask_login import login_user, current_user, logout_user, login_required
from fantasybasketball.authentication import SignUpForm, SignInForm
from flask_login import LoginManager

@app.route('/', methods=['GET', 'POST'])
def start():
    return redirect('/about')

@app.route('/about', methods=['GET', 'POST'])
def display():
    return render_template('about.html')

@app.route('/home', methods=['GET', 'POST'])
def display2():
    return "<h1> Home Page </h1>"

@app.route('/favorites', methods=['GET', 'POST'])
def display3():
    return ""

@app.route('/signin',methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    else:
        user_form = SignInForm()
        if user_form.validate_on_submit():
            # check if the data submitted by the user is correct
            cur = mysql.connection.cursor()
            cur.execute('''SELECT Username, Password FROM Scouts''')
            rows = cur.fetchall()
            for row in rows:
                if row[0] == user_form.username.data and row[1] == user_form.password.data:
                    login_user(user)
                    next_page = request.args.get('next')
                    if next_page:
                        redirect(next_page)
                    else:
                        redirect('/home')
            flash('wrong sign in.', 'fail')
        return render_template('signin.html', form=user_form)

@app.route('/signout',methods=['GET', 'POST'])
def signout():
    return redirect('/about')

@app.route('/signup',methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    else:
        user_form = SignUpForm()
        if user_form.validate_on_submit() and valid_team(user_form.team.data):
            # Insert the new scout's attributes into database
            cur = mysql.connection.cursor()
            cur.execute("""INSERT INTO Scouts VALUES (%s, %s, %s, %s)""", (user_form.email.data, user_form.username.data, user_form.password.data, user_form.team.data))
            mysql.connection.commit()
            cur.close()
            flash('account created.', 'success')
            return redirect(url_for('signin'))
        else:
            # account has invalid team or invalid input
            return render_template('signup.html', form=user_form)

def valid_team(team):
    cur = mysql.connection.cursor()
    cur.execute('''SELECT TeamName FROM Teams''')
    rows = cur.fetchall()
    teamExists = False
    for row in rows:
        if row[0] == team:
            return True
    return False
