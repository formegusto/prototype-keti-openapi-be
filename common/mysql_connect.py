import pymysql
import json

mysql_info_file = open("auth/mysql_info.json", "r", encoding="utf8")
mysql_info = json.load(mysql_info_file)

MYSQL_CONN = pymysql.connect(
    host=mysql_info['HOST'],
    port=mysql_info['PORT'],
    user=mysql_info['USER'],
    password=mysql_info['PASSWORD'],
    database=mysql_info['DB'],
)


def conn_mysqldb():
    if not MYSQL_CONN.open:
        MYSQL_CONN.ping(reconnect=True)
    return MYSQL_CONN
