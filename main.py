from sqlite3.dbapi2 import Cursor
from flask import Flask, render_template, g
import sqlite3 


app=Flask(__name__)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect("pcinfo.db")
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()




@app.route('/')
def home():
    return render_template('home.html', title = "home")


@app.route('/cpu')
def cpu():
    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM Cpu ;" )
    results = cursor.fetchall()
    return render_template('cpu.html', results=results)
    

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/parts')
def parts():
    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM Chasis ;" )
    case = cursor.fetchall()
    return render_template('parts.html', case=case)

if __name__ == '__main__':
    app.run(debug=True)