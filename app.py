from flask import Flask,render_template
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['MYSQL_USER'] = 'sql3356970'
app.config['MYSQL_PASSWORD'] = 'gAgxITG1pb'
app.config['MYSQL_HOST'] = 'sql3.freemysqlhosting.net'
app.config['MYSQL_DB'] = 'sql3356970'
app.config['MYSQL_CURSURCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def index():

    cur = mysql.connection.cursor()
    return render_template("index.html")
