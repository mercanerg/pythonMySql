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
dbcursor.execute("SELECT * FROM products")
result = dbcursor.fetchall()
# result = dbcursor.fetchone()  # print only one record
for i in result:
  print(i[0], "$", i[1])
print("The sum of records = ", dbcursor.rowcount)

del_product = (input("enter the product name will be deleted - > "),)
sql = "DELETE FROM products WHERE name = %s"
dbcursor.execute(sql, del_product)
print("\n ---------------------------")
dbcursor.execute("SELECT * FROM products")
result = dbcursor.fetchall()
# result = dbcursor.fetchone()  # print only one record
for i in result:
  print(i[0], "$", i[1])

con.commit()
print("The sum of records = ", dbcursor.rowcount)