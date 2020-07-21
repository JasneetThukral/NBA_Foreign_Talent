from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>This is Fantasy Basketball <h1>'

@app.route('/about')
def about_page():
    return '<h1>hihihi<h1>'

if __name__ == '__main__':
    app.run(debug=True)
