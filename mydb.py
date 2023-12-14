import mysql.connector


data_base = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123'
)

#preparar objeto cursor 

cursor_object = data_base.cursor()

#crear db
cursor_object.execute("CREATE DATABASE test_corp")

print('todo ok')