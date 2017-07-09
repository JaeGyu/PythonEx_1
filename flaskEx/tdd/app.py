import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
      abort, render_template, flash, jsonify

#설정
DATABASE = 'flaskr.db' 
DEBUG = True
SECRET_KEY = 'my_precious'
USER ='admin'
PASSWORD = 'admin'

app = Flask(__name__)
app.config.from_object(__name__)


# @app.route("/")
# def hello():
#     return "Hello, World!"

if __name__ == "__main__":
    app.run()