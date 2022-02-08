import os
from sqlite3 import connect
import pymysql

username = "root"
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             database='Chinook')




try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()

