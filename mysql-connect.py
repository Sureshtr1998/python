# pip install mysql-connector-python

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root",database="surecode", password="1234")

mycursor = mydb.cursor()

# mycursor.execute("show databases")
mycursor.execute("select * from student")

result = mycursor.fetchall()
print(result)

# for i in mycursor:
for i in result:

    print(i)