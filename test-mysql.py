import mysql.connector

mydb = mysql.connector.connect(
    host="192.168.2.112",
    database="logs",
    user="logs",
    password="???",
    autocommit=True
)

mycursor = mydb.cursor()

sql = "INSERT INTO webapp (event_time, app_name, score) VALUES (%s, %s, %s)"
val = ('2023-02-19 13:13:24', 'test2', 4.123)
mycursor.execute(sql, val)
print(mycursor.rowcount, "record inserted")
mycursor.close()