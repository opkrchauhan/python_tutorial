import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2022988"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")