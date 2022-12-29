#!/usr/bin/python3
"""lists all states from the hbtn_0e_0_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           password=sys.argv[2], db=sys.argv[3], port=3306,
                           charset="utf8")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states")
    query = cursor.fetchall()
    for states in query:
        print(states)
    cursor.close()
    conn.close()
