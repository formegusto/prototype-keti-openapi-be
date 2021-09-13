from flask import request as req
from flask_restx import Namespace, Resource
from models.user_info import USER_INFO

AUTH = Namespace("auth api")


@AUTH.route("")
class AuthAPI(Resource):
    def post(self):
        return "Login API"


@AUTH.route("/join")
class JoinAPI(Resource):
    def post(self):
        body = req.json

        USER_INFO.create(body['userId'], body['password'])
        return "Join API"
