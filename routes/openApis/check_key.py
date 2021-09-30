import bcrypt
from flask import request as req


def check_key(func):
    def _check_key(*args, **kargs):
        accessKey = req.args.get("accessKey")

        if accessKey == None:
            return {"message": "accessKey가 반드시 필요합니다."}, 401

        return func(*args, **kargs)
    return _check_key
