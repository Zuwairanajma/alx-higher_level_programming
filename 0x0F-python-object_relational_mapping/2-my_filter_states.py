#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
using the first three arguments passed as user credentials

1st arg: user
2nd arg: password
3rd arg: database

"""

import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           password=sys.argv[2], db=sys.argv[3], port=3306,
                           charset="utf8")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'".format(
                                                            sys.argv[4]))
    query = cursor.fetchall()
    for states in query:
        print(states)
    cursor.close()
    conn.close()
