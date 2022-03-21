""" Copyright RCN Soft - Mehmet Ercan EREGLIOGLU
    Module consists of connecting MySQL,
    and, if there is no database or table, generating them"""

import mysql.connector


try:
#create a new connection
    con = mysql.connector.connect(
        host = "host_name",
        username = 'your_user_name',
        password = 'your_password')
except:
    print('MySql connection error!')

dbase = 'rcndbase'
dbcursor = con.cursor()
dbcursor.execute('SHOW DATABASES')
print('Data base list in MySQL')
is_control = False
#check if dbase created
for x in dbcursor:
    if x[0]==dbase:
        is_control = True
    print(x[0])
if not is_control:
    dbcursor.execute("CREATE DATABASE rcnDbase")
print()

try:
#create a new connection
    con = mysql.connector.connect(
        host = "localhost",
        username = 'root',
        password = 'MarWeg...01',
        database = 'rcnDbase')
except:
    print('DATABASE connection error!')
dbcursor = con.cursor()
dbcursor.execute("SHOW TABLES")
is_control = False
rcn_table = 'products'
print(f'Table list in {dbase}')
for i in dbcursor:
    if i[0] == rcn_table:
        is_control = True
    print(i[0])
sql = "CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price int)"
if not is_control:
    dbcursor.execute(sql)
con.commit()
dbcursor.close()
con.close()

