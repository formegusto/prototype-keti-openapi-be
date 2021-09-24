from flask import request as req
from flask_restx import Namespace, Resource
from models.open_api import OPEN_API

OPENAPI = Namespace("open-api api")


@OPEN_API.route("/join/<int:api_id>")
class JoinOpenAPI(Resource):
    def post(self, api_id):
        return "Success!"


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
