from flask import Blueprint, jsonify, request
from .models import db
from .models import *
# coding: utf-8

api = Blueprint('api', __name__)


@api.route('/hoge/<string:str>', methods=["GET"])
def hogeGet(str):
    return "hogeGet: " + str


@api.route("/hoge", methods=["POST"])
def hogePost():
    text = request.form["text"]
    return "hogePost: " + text


# レコード全取得APIの例
@api.route("/test", methods=["GET"])
def test():
    test_list = db.session.query(Test).all()
    test_dict = [test.to_dict() for test in test_list]
    return jsonify(test_dict)

# 新規登録用API
@api.route("/registration", methods=["POST"])
def new_regstration():
    if "name" in request.form:
        user_name = request.form["name"]
    else:
        return "error: not found name"

    if len(db.session.query(Users.user_name).filter(
            Users.user_name == user_name).all()) != 0:
        return "this user name is exist"

    if "email" in request.form:
        user_email = request.form["email"]
    else:
        return "error: not found email"

    if len(db.session.query(Users.user_name).filter(
            Users.email == user_email).all()) != 0:
        return "this email address is exist"

    if "password" in request.form:
        password = request.form["password"]
    else:
        return "error: not found password"

    user_data = [Users(
        email=user_email,
        user_name=user_name,
        password=password
    )]

    db.session.add_all(user_data)
    db.session.commit()

    return "complete registration"


# login認証をするAPI
@api.route("/login", methods=["POST"])
def login():
    user_email = ""
    password = ""
    if "email" in request.form:
        user_email = request.form["email"]
    else:
        return "error: not found email"

    if "password" in request.form:
        password = request.form["password"]
    else:
        return "error: not found password"

    user_name = db.session.query(
        Users.user_name).filter(
        Users.email == user_email,
        Users.password == password).all()
    if len(user_name) == 0:
        return "permission denied"

    user_name = user_name[0][0]
    return str(user_name)
