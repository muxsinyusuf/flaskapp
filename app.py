#!/usr/bin/env python3
from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    response_body = "<h1>Hello world</h1>"
    status = 200
    headers = {}
    return make_response(response_body, status, headers)


@app.route('/users', methods=['GET', 'POST','PATCH','DELETE'])
def manage_users():
    if request.method == "GET":
        users = []
        for user in User.query.all():
            user_dict = {
                "name": user.name
            }
            users.append(user_dict)

        response = make_response(
            jsonify(users),
            200
        )
        return response

    elif request.method == "POST":
        data = request.get_json()
        new_user = User(
            name=data.get("name")
        )

        db.session.add(new_user)
        db.session.commit()

        user_dict = {
            "name": new_user.name
        }

        response = make_response(
            jsonify(user_dict),
            201
        )

        return response        
    elif request.method == "DELETE":
        db.session.delete(id)
        db.session.commit()

        response_body={
            "delete_successful": True,
            "deleted_user_id": id

        }
        response = make_response(
            jsonify(response_body),
            200
        )

        return response



    


@app.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    user = User.query.filter_by(id=id).first()
    if user:
        user_dict = {"name": user.name}
        return jsonify(user_dict), 200


if __name__ == '__main__':
    app.run(port=5555)
