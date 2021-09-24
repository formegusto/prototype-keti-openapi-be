from flask import request as req

from flask_restx import Namespace, Resource
from models.api_grp import API_GRP

APIGRP = Namespace("api-group api")


@APIGRP.route("")
class ApiGrpAPI(Resource):
    def post(self):
        body = req.json

        API_GRP.create(body['name'], body['title'])
        return "ApiGrp API"
