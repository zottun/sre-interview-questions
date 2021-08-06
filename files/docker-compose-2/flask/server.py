#!/usr/bin/env python
import os

from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongo:{}".format(os.environ.get("MONGO_SERVER_PORT", 27017)))


@app.route('/')
def todo():
    try:
        client.admin.command('ismaster')
    except:
        return "Mongo Server unavailable"
    return 'Hello World!\n'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)
