import json
from flask import Flask
from flask_restx import Api, Resource

# API LIST
from routes.auth_routes import AUTH
from routes.apigrp_routes import APIGRP
from routes.openapi_routes import OPENAPI
from routes.openApis.hp_routes import HOUSEHOLDPOWER

app = Flask(__name__)
api = Api(app)

secret_file = open("auth/secret.json", "r", encoding="utf8")
jwt_key = json.load(secret_file)['jwt_key']

api.add_namespace(AUTH, "/auth")
api.add_namespace(APIGRP, "/apigroup")
api.add_namespace(OPENAPI, "/openapi")

# OPEN_APIs
api.add_namespace(HOUSEHOLDPOWER, "/household_power")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
