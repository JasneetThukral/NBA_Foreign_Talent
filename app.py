from flask import Flask, render_template
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['MYSQL_USER'] = 'sql3356970'
app.config['MYSQL_PASSWORD'] = 'gAgxITG1pb'
app.config['MYSQL_HOST'] = 'sql3.freemysqlhosting.net'
app.config['MYSQL_DB'] = 'sql3356970'
app.config['MYSQL_CURSURCLASS'] = 'DictCursor'

mysql = MySQL(app)

class Players(db.Model):
    PlayerID = db.Column(db.Integer, primary_key=True)
    PlayerName = db.Column(db.String(550), nullable=False)
    TeamName = db.Column(db.String(300), db.ForeignKey(Teams.TeamName), nullable=False)
    Positions = db.Column(db.String(10), nullable=False)
    Height = db.Column(db.Integer, nullable=False)
    Weight = db.Column(db.Integer, nullable=False)

class Teams(db.Model):
    pass

class Statistics(db.Model):
    PlayerID = db.Column(db.Integer, db.ForeignKey(Players.PlayerID))
    numGames = db.Column(db.Integer, nullable=False)
    

class Leagues(db.Model):
    LeagueName = db.Column(db.String(250), unique=True, nullable=False)
    NumGames = db.Column(db.Integer)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    return render_template('index.html')
