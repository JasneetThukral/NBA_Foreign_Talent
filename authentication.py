from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from fantasybasketball import app, mysql
import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

class SignUpForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=5, max=10)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    team = StringField('Team',
                        validators=[DataRequired(), Length(min=2, max=30)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def username_exists(self, username):
        cur = mysql.connection.cursor()
        cur.execute('''SELECT Username FROM Scouts''')
        rows = cur.fetchall()
        for row in rows:
            if str(row[0]) == username.data:
                raise ValidationError('Username already has account')

    def email_exists(self, email):
        cur = mysql.connection.cursor()
        cur.execute('''SELECT Email FROM Scouts''')
        rows = cur.fetchall()
        for row in rows:
            if str(row[0]) == email.data:
                raise ValidationError('Email already has account')

class SignInForm(FlaskForm):
    username = StringField('Username',
                        validators=[DataRequired(), Length(min=5, max=10)])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Sign In')
