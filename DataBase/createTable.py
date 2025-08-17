import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2022988",
    database="mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)")
print("Table created successfully")
