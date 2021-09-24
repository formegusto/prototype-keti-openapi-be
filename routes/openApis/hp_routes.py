# household_power API routes
from flask_restx import Namespace, Resource
from models.openApis.household_power import HOUSEHOLD_POWER as HPDB

HOUSEHOLDPOWER = Namespace("open-api: household_power api")


@HOUSEHOLDPOWER.route("")
class HouseholdPowerAPI(Resource):
    def get(self):
        return {
            "data": HPDB.find()
        }
