import jwt
import json
from flask import request as req
from flask_restx import Namespace, Resource
from models.user_info import USER_INFO

AUTH = Namespace("auth api")

secret_file = open("auth/secret.json", "r", encoding="utf8")
jwt_key = json.load(secret_file)['jwt_key']


def check(func):
    def _check(*args, **kargs):
        header = req.headers.get("Authorization")
        if header == None:
            return {"message": "로그인이 필요한 서비스 입니다."}, 401
        try:
            data = jwt.decode(header, jwt_key, algorithms="HS256")
        except:
            return {"message": "올바르지 않은 인증 입니다."}, 401

        return func(*args, **kargs)
    return _check


def get_user_by_token(token):
    return jwt.decode(token, jwt_key, algorithms="HS256")


@AUTH.route("")
class AuthAPI(Resource):
    def post(self):
        body = req.json

        user, msg, status = USER_INFO.find(body['userId'], body['password'])

        if user == None:
            return {
                "message": msg
            }, status
        else:
            return {
                "token": jwt.encode({
                    "user_id": user[1],
                }, jwt_key, algorithm="HS256")
            }, status


@AUTH.route("/join")
class JoinAPI(Resource):
    def post(self):
        body = req.json

        USER_INFO.create(body['userId'], body['password'])
        return {"success": True}, 200
