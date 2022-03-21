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

sql = "SELECT * FROM products ORDER BY name"
dbcursor.execute(sql)
result = dbcursor.fetchall()
for i in result:
    print(i[0], "\t", "$", i[1])

sql = "SELECT * FROM products WHERE name = %s"
val = (input("enter name what you update == > "),)
update_sate = True
try:
    dbcursor.execute(sql, val)
    result = dbcursor.fetchall()
    print(f"product name:{result[0][0]}     price:${result[0][1]}")

except:
    print("couldn't find a product you searched")
    update_sate = False

if update_sate:
    try:
        name = input("enter new name  == > ")
        price = input("enter new price == > ")
        sql = "Update products set name = %s where price = %s"
        val = (name, price)
        dbcursor.execute(sql, val)
        con.commit()
    except:
        print("an Error in updating")


dbcursor.close()