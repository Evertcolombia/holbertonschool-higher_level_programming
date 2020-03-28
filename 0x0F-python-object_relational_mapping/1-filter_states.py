#!/usr/bin/python3
import sys
import MySQLdb

"""
    Script to conect to a sql db using MySQLdb client in python
"""

if len(sys.argv) != 4:
    print("arguments must be 3")
    sys.exit(1)
else:
    usrn = sys.argv[1]
    passw = sys.argv[2]
    db_name = sys.argv[3]
    hos_t = "localhost"

    db = MySQLdb.connect(host=hos_t, user=usrn,  passwd=passw, db=db_name)
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE (name REGEXP '^N')")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
