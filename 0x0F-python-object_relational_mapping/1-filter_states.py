#!/usr/bin/python3
'''This script list states with a name starting with N (upper N)'''
import sys
import MySQLdb

if len(sys.argv) == 4:
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    mydb = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        database=database
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM states WHERE (name REGEXP '^N')")
    myresult = mycursor.fetchall()

    for data in myresult:
        print(data)

    mycursor.close()
