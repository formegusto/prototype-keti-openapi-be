from common.mysql_connect import conn_mysqldb


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
