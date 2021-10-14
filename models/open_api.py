from common.mysql_connect import conn_mysqldb
import datetime as dt
import bcrypt

OPEN_API_COLUMNS = ["id", "name", "title", "content", "restUri", "grpId"]
USE_OPEN_API_COLUMNS = ["id", "name", "title",
                        "content", "restUri", "grpId", "accessKey"]


class OPEN_API():
    def __init__(self, name, title, content, rest_uri, grp_id):
        self.name = name
        self.title = title
        self.content = content
        self.rest_uri = rest_uri
        self.grp_id = grp_id

    @staticmethod
    def create(name, title, content, rest_uri, grp_id):
        db = conn_mysqldb()
        db_cursor = db.cursor()

        sql = "INSERT INTO OPEN_API("\
            + "name, title, content, restUri, grpId) "\
            + "VALUES('{}', '{}', '{}', '{}', '{}');"\
            .format(name, title, content, rest_uri, grp_id)

        db_cursor.execute(sql)
        db.commit()

    @staticmethod
    def find(api_id):
        db = conn_mysqldb()
        db_cursor = db.cursor()

        sql = "SELECT * "\
            + "FROM OPEN_API "\
            + "WHERE ID='{}'".format(api_id)

        db_cursor.execute(sql)
        open_api_info = db_cursor.fetchone()

        return open_api_info

    @staticmethod
    def find_all_by_grpId(grp_id):
        db = conn_mysqldb()
        db_cursor = db.cursor()

        sql = "SELECT * "\
            + "FROM OPEN_API "\
            + "WHERE grpId='{}'".format(grp_id)
        db_cursor.execute(sql)
        db_datas = db_cursor.fetchall()

        all_api = list()
        for data in db_datas:
            in_dict = dict()
            for idx, _ in enumerate(data):
                in_dict[OPEN_API_COLUMNS[idx]] = _
            all_api.append(in_dict)

        return all_api

    @staticmethod
    def find_api_grp(api_name):
        db = conn_mysqldb()
        db_cursor = db.cursor()

        sql = "SELECT * "\
            + "FROM API_GROUP "\
            + "WHERE name='{}'".format(api_name)
        db_cursor.execute(sql)
        api_group = db_cursor.fetchone()

        return api_group

    @staticmethod
    def find_use_apis(user_id):
        db = conn_mysqldb()
        db_cursor = db.cursor()

        use_sql = "SELECT * "\
            + "FROM USER_USE_OPEN_API "\
            + "WHERE userID={}".format(user_id)
        db_cursor.execute(use_sql)
        uses = db_cursor.fetchall()

        if uses == None:
            return None

        use_apis = list()
        for use_api in uses:
            in_dict = dict()

            api_id = use_api[1]
            api = OPEN_API.find(api_id)

            for idx, _ in enumerate(api):
                in_dict[USE_OPEN_API_COLUMNS[idx]] = _
            in_dict[USE_OPEN_API_COLUMNS[6]] = use_api[2]
            use_apis.append(in_dict)

        return use_apis

    @staticmethod
    def check_used(api_id, user_id, access_key):
        db = conn_mysqldb()
        db_cursor = db.cursor()

        sql = "SELECT * "\
            + "FROM USER_USE_OPEN_API "\
            + "WHERE userId='{}' ".format(user_id)\
            + "AND apiId='{}' ".format(api_id)\
            + "AND accessKey='{}'".format(access_key)

        db_cursor.execute(sql)
        is_used = db_cursor.fetchone()

        return is_used

    @staticmethod
    def check_registed(api_id, user_id):
        db = conn_mysqldb()
        db_cursor = db.cursor()

        sql = "SELECT * "\
            + "FROM USER_USE_OPEN_API "\
            + "WHERE userId='{}' ".format(user_id)\
            + "AND apiId='{}'".format(api_id)

        db_cursor.execute(sql)
        is_registed = db_cursor.fetchone()

        return is_registed

    @staticmethod
    def regist(api_id, user):
        db = conn_mysqldb()
        db_cursor = db.cursor()

        now_time = dt.datetime.now().timestamp()
        user_id, user_name = user[0], user[1]

        token_info = "{}&{}&{}".format(now_time, user_id, user_name)
        access_key = bcrypt.hashpw(token_info.encode(
            "utf-8"), bcrypt.gensalt()).decode("utf-8")

        sql = "INSERT INTO USER_USE_OPEN_API("\
            + "userId, apiId, accessKey) "\
            + "VALUES ('{}', '{}', '{}')"\
            .format(user_id, api_id, access_key)
        print(sql)
        db_cursor.execute(sql)
        db.commit()

        return access_key
