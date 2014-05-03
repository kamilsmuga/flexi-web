import os
from flask import Flask
import couchdb

app = Flask(__name__)

@app.route('/')
def hello():
    return 'flexi.note says hello!'

@app.route('/couch')
def test():
    couch = couchdb.Server()
    db = couch.create('test')
    print db
    db['foo'] = {'bar' : 'test'}
    return db['foo']
