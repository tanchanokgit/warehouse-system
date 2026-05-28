import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3307,
    user='warehouse_user',
    password='1234',
    database='warehouse'
)

cursor = conn.cursor()
cursor.execute("SHOW DATABASES;")
print(cursor.fetchall())