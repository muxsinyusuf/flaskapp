#!/usr/bin/env python3
from flask import Flask, make_response
from flask_migrate import Migrate
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    response_body = "<h1>Hello world</h1>"
    status = 200
    headers = {}
    return make_response(response_body, status, headers)

if __name__ == '__main__':
    app.run(port=5555)
