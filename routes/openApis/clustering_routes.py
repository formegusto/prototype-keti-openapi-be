# household_power API routes
from flask import request as req
from routes.auth_routes import check, get_user_by_token
from routes.openApis.check_key import check_key
from flask_restx import Namespace, Resource
from models.openApis.clustering import CLUSTERING as CLDB
from models.open_api import OPEN_API
from models.user_info import USER_INFO

CLUSTERING = Namespace("open-api: clustering api")
CLUSTERING_ID = 4


@CLUSTERING.route("")
class ClusteringAPI(Resource):
    @check_key
    def get(self):
        access_key = req.args.get("accessKey")
        user = USER_INFO.findByAccessKey(access_key)

        if user == None:
            return {
                "message": "API를 신청해주세요."
            }, 401

        is_used = OPEN_API.check_used(CLUSTERING_ID, user[0], access_key)

        if is_used == None:
            return {
                "message": "API를 신청해주세요."
            }, 401

        return {
            "data": CLDB.find()
        }, 200
