import mysql.connector

try:
#create a new connection
    con = mysql.connector.connect(
        host="host_name",
        username='your_user_name',
        password='your_password',
        database = "databe_name")
except:
    print('MySql or rcndbase connection error!')

dbcursor = con.cursor()
sql = "INSERT INTO products (name, price) VALUES (%s, %s)"

product_name = input("input the name of product > ")
price = int(input("input the price of product > "))
val = (product_name, price)
dbcursor.execute(sql, val)  # inserting just one row

# val = [('coca cola 33cc', 1), ('Nescafe 5gr x 25unit', 5)]
# dbcursor.executemany(sql, val) # add multi rows into table

idnum = dbcursor.lastrowid
rcount = dbcursor.rowcount
con.commit()
print(f" {rcount} row is added into table")
dbcursor.execute("SELECT * FROM products")
result = dbcursor.fetchall()
# result = dbcursor.fetchone()  # print only one record
for i in result:
  print(i[0], i[1], "$", i[2])

print(f"listed {dbcursor.rowcount} rows")
con.commit()
dbcursor.close()
con.close()
