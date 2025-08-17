import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2022988",
    database="mydatabase"
)

mycursor = mydb.cursor()
sql ="Select * FROM users where id =2"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for row in myresult:
    print(row)