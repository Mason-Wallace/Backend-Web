from flask import Flask
import datetime
from datetime import time

app = Flask(__name__)

@app.route("/")
def index():
    return "<p><a href='/'>Home</a> | <a href='/second'>Second</a> | <a href='/hour'>Hour</a> | <a href='/year'>Year</a></p>"

@app.route("/second")
def second():
    date = datetime.datetime.today()
    second = date.second
    return f"<p>The second is: { second }</p> <br> <p><a href = '/'>Home</a>"

@app.route("/hour")
def hour():
    date = datetime.datetime.today()
    hour = date.hour 
    return f"<p>The hour is: { hour }</p> <br> <p><a href = '/'>Home</a>"

@app.route("/year")
def year():
    date = datetime.date.today()
    year = date.year
    return f"<p>The year is: { year }</p> <br> <p><a href = '/'>Home</a>"

if __name__ == '__main__':
    app.run(debug=True)