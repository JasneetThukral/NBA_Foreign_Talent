from flask import Flask, render_template,request
from flask_mysqldb import MySQL


app = Flask(__name__,template_folder='templates')
app.config['MYSQL_USER'] = 'sql3356970'
app.config['MYSQL_PASSWORD'] = 'gAgxITG1pb'
app.config['MYSQL_HOST'] = 'sql3.freemysqlhosting.net'
app.config['MYSQL_DB'] = 'sql3356970'
app.config['MYSQL_CURSURCLASS'] = 'DictCursor'

mysql = MySQL(app)
table = ""

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == "POST":
        details = request.form
        query = details['statement']
        table = details['table']
        cur = mysql.connection.cursor()
        row = cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print(row)
        mysql.connection.commit()
        cur.close()
        print(query)
    return render_template('index.html')


@app.route('/results',methods=['GET', 'POST'])
def script_output():
    cur = mysql.connection.cursor()
    # if str(table) == "Players":
    print(table)
    cur.execute("SELECT * FROM Players")
    rows = cur.fetchall()
    print(rows)
    return render_template('results.html',output=rows)
if __name__ == 'main':
    app.run(debug=True)
