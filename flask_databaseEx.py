from flask import Flask
import sqlite3

DATABASE = "/Users/jaegyuhan/dev/sqlite3/books.db"

app = Flask(__name__)

app.config.from_object(__name__)


