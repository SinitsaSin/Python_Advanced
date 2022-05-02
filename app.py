import sqlite3
import html
from flask import Flask, render_template
from werkzeug.exceptions import abort
from variables import URL, DEBUG, PORT

app = Flask(__name__)


def get_db_connection():
    connection = sqlite3.connect(URL)
    connection.row_factory = sqlite3.Row
    return connection

def get_name(name_id):
    connection = get_db_connection()
    name = connection.execute('SELECT * FROM customers WHERE CustomerId = ?', (name_id, )).fetchone()
    connection.close()
    if name is None:
        abort(404)
    else:
        return name

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/name")
def list_name():
    connection = get_db_connection()
    names = connection.execute('SELECT * FROM customers;').fetchall()
    connection.close()
    return render_template('example.html', names=names)

app.run(debug=DEBUG, port=PORT)