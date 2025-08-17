import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2022988",
    database="mydatabase"
)

mycursor = mydb.cursor()
sql = "INSERT INTO users (name, age) VALUES (%s, %s)"
values = ("John Doe", 30)
mycursor.execute(sql, values)
mydb.commit()

print(mycursor.rowcount, "record inserted.")
