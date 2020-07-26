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
    cur_two = mysql.connection.cursor()
    cur_three = mysql.connection.cursor()
    cur_four = mysql.connection.cursor()
    # if str(table) == "Players":
    output_one = cur.execute("SELECT * FROM Players")
    output_two = cur_two.execute("SELECT * FROM Statistics")
    output_three = cur_three.execute("SELECT * FROM Leagues")
    output_four = cur_four.execute("SELECT * FROM Teams")
    rows = cur.fetchall()
    row_two = cur_two.fetchall()
    row_three = cur_three.fetchall()
    row_four = cur_four.fetchall()
    print(rows)
    return render_template('results.html',output_one=rows,output_two=row_two,output_three=row_three,output_four=row_four)
if __name__ == 'main':
    app.run(debug=True)
