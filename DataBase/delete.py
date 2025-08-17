import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="2022988",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM users WHERE id=1"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")