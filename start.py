import os
from flask import Flask
import couchdb
import logging

app = Flask(__name__)
logging.basicConfig(filename='debug.log', level=logging.INFO)

@app.route('/')
def hello():
    print 'hello'
    return 'flexi.note says hello!'

@app.route('/couch')
def test():
    print 'test'
    logging.info("i'm in /couch")
    couch = couchdb.Server()
    logging.info("couch server created")
    db = couch.create('test')
    logging.info("db test created")
    logging.info(db)
    db['foo'] = {'bar' : 'test'}
    logging.info(db['foo'])
    return db['foo']
