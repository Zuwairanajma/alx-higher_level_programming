#!/usr/bin/python3
"""
lists states that its name starts with N
user credentials and dabase are passed as argument
"""

import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306,
                           charset="utf8")
    cursor = conn.cursor()
    cursor.execute("""
            SELECT * FROM states
            WHERE name LIKE BINARY 'N%'
            ORDER BY states.id""")
    query = cursor.fetchall()
    for states in query:
        print(states)
    cursor.close()
    conn.close()
