#!/usr/bin/python3
"""
eLists all cities of a state from the database hbtn_)e_4_usa
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
    state = sys.argv[4]
    cursor = conn.cursor()
    cursor.execute("""SELECT cities.name
                   FROM cities JOIN states ON cities.state_id = states.id
                   WHERE states.name = %s""", (state,))
    query = cursor.fetchall()
    city_names = []
    for state in query:
        city_names.append(state[0])
    print(*city_names, sep=", ")
    cursor.close()
    conn.close()
