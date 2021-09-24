from common.mysql_connect import conn_mysqldb


class API_GRP():
    def __init__(self, name, title):
        self.name = name
        self.title = title

    @staticmethod
    def create(name, title):
        db = conn_mysqldb()
        db_cursor = db.cursor()

        sql = "INSERT INTO API_GROUP("\
            + "name, title) "\
            + "VALUES('{}', '{}');".format(name, title)

        db_cursor.execute(sql)
        db.commit()
