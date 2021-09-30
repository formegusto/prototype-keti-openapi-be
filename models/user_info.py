import bcrypt
from common.mysql_connect import conn_mysqldb


class USER_INFO():
    def __init__(self, id, user_id):
        self.id = id
        self.user_id = user_id

    @staticmethod
    def create(user_id, password):
        db = conn_mysqldb()
        db_cursor = db.cursor()

        hash_password = bcrypt.hashpw(password.encode(
            "utf-8"), bcrypt.gensalt()).decode("utf-8")
        sql = "INSERT INTO USER_INFO("\
            + "userId, password) "\
            + "VALUES('{}', '{}');".format(user_id, hash_password)

        db_cursor.execute(sql)
        db.commit()

    @staticmethod
    def find(user_id, password):
        db = conn_mysqldb()
        db_cursor = db.cursor()

        sql = "SELECT * "\
            + "FROM USER_INFO "\
            + "WHERE userId='{}'".format(user_id)

        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        db_password = user[2]

        if user == None:
            return None, "등록되지 않은 계정입니다.", 404
        elif not bcrypt.checkpw(password.encode('utf-8'), db_password.encode('utf-8')):
            return None, "올바르지 않은 정보입니다.", 401
        else:
            # user_id
            return user, "로그인 성공", 200

    @staticmethod
    def findById(user_id):
        db = conn_mysqldb()
        db_cursor = db.cursor()

        sql = "SELECT * "\
            + "FROM USER_INFO "\
            + "WHERE userId='{}'".format(user_id)

        db_cursor.execute(sql)
        user = db_cursor.fetchone()

        return user
