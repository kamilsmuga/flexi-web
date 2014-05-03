import os
from flask import Flask
import couchdb
import logging

app = Flask(__name__)
logging.basicConfig(filename='debug.log', level=logging.INFO)
KUROBASE_BUCKET = os.environ['KUROBASE_BUCKET']
KUROBASE_PASS = os.environ['KUROBASE_PASS']
KUROBASE_SERVER = os.environ['KUROBASE_SERVER']
KUROBASE_URL = os.environ['KUROBASE_URL']

@app.route('/')
def hello():
    print 'hello'
    return 'flexi.note says hello!'

@app.route('/couch')
def test():
    print 'test'
    logging.info("i'm in /couch")
    couch = couchdb.Server(url="http://"+KUROBASE_BUCKET+":"+KUROBASE_PASS+"@"+KUROBASE_URL)
    print 'dupa'
    logging.info("couch server created")
    db = couch.create('test')
    print '2 dupy'
    logging.info("db test created")
    logging.info(db)
    db['foo'] = {'bar' : 'test'}
    logging.info(db['foo'])
    return db['foo']

if __name__ == '__main__':
    app.run(debug=True)
