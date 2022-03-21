import mysql.connector

# create a new connection
try:
    con = mysql.connector.connect(
        host="host_name",
        username='your_user_name',
        password='your_password',
        database="databe_name")
except:
    print('MySql or rcndbase connection error!')

dbcursor = con.cursor()
dbcursor.execute("DROP TABLE products")