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
