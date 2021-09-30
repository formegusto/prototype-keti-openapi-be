from routes.auth_routes import check, get_user_by_token
from flask import request as req
from flask_restx import Namespace, Resource
from models.open_api import OPEN_API
from models.user_info import USER_INFO

OPENAPI = Namespace("open-api api")


@OPENAPI.route("/join/<int:api_id>")
class JoinOpenAPI(Resource):
    @check
    def post(self, api_id):
        open_api_info = OPEN_API.find(api_id)

        if open_api_info == None:
            return {"message": "존재하지 않는 API 입니다."}, 404

        # find User
        token = req.headers.get("Authorization")
        token_data = get_user_by_token(token)
        user = USER_INFO.findById(token_data['user_id'])

        # registed check
        is_registed = OPEN_API.check_registed(api_id, user[0])
        if is_registed != None:
            return {"message": "이미 등록된 API 입니다."}, 401

        access_key = OPEN_API.regist(api_id, user)

        return {
            "accessKey": access_key
        }, 201


@OPENAPI.route("/<int:grp_id>")
class OpenAPI(Resource):
    def post(self, grp_id):
        body = req.json

        OPEN_API.create(
            body['name'],
            body['title'],
            body['content'],
            body['restUri'],
            grp_id
        )

        return "Success!"


@OPENAPI.route("/user")
class OpenAPIUser(Resource):
    @check
    def get(self):
        token = req.headers.get("Authorization")
        token_data = get_user_by_token(token)

        user = USER_INFO.findById(token_data['user_id'])
        use_apis = OPEN_API.find_use_apis(user[0])

        return {
            "data": use_apis
        }, 200


@OPENAPI.route("/service")
class OpenAPIService(Resource):
    def get(self):
        name = req.args.get("name")
        api_group = OPEN_API.find_api_grp(name)

        if api_group == None:
            return {
                "message": "존재하지 않는 API 그룹입니다."
            }, 404

        return {
            "data": OPEN_API.find_all_by_grpId(api_group[0])
        }, 200


@OPENAPI.route("/service/<int:api_id>")
class OpenAPIServiceDetail(Resource):
    def get(self, api_id):
        api = OPEN_API.find(api_id)

        if api == None:
            return {
                "message": "존재하지 않는 API 입니다."
            }, 404

        return {
            "data": api
        }, 200
