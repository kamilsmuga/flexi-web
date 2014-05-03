import os
from flask import Flask
import couchdb
import logging

app = Flask(__name__)

COUCH_URL = "http://localhost:8092"

@app.route('/')
def hello():
    print 'hello'
    return 'flexi.note says hello!'

@app.route('/couch')
def test():
    couch = couchdb.Server(url=COUCH_URL)
    db = couch.create('flexidb')
    db['foo'] = {'bar' : 'test'}
    return db['foo']

if __name__ == '__main__':
    app.run(debug=True)
