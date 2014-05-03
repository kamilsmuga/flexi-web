import os
from flask import Flask
import couchdb

app = Flask(__name__)

@app.route('/')
def hello():
    return 'flexi.note says hello!'
