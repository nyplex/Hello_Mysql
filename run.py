import datetime
import pymysql

username = "root"
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             database='Chinook')




try:
    with connection.cursor() as cursor:
        rows = [(18, 'Bob'),
                (34, 'Jim'),
                (95, 'Albert')]
        cursor.execute("DELETE FROM Friends WHERE name = 'Bob';")
        connection.commit()
        
finally:
    connection.close()

