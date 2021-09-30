# household_power API routes
from flask import request as req
from routes.auth_routes import check, get_user_by_token
from routes.openApis.check_key import check_key
from flask_restx import Namespace, Resource
from models.openApis.household_power import HOUSEHOLD_POWER as HPDB
from models.open_api import OPEN_API
from models.user_info import USER_INFO

HOUSEHOLDPOWER = Namespace("open-api: household_power api")
HOUSEHOLDPOWER_ID = 2


@HOUSEHOLDPOWER.route("")
class HouseholdPowerAPI(Resource):
    @check
    @check_key
    def get(self):
        access_key = req.args.get("accessKey")
        token = req.headers.get("Authorization")

        token_data = get_user_by_token(token)
        user = USER_INFO.findById(token_data['user_id'])

        is_used = OPEN_API.check_used(HOUSEHOLDPOWER_ID, user[0], access_key)

        if is_used == None:
            return {
                "message": "API를 신청해주세요."
            }, 401

        return {
            "data": HPDB.find()
        }, 200
