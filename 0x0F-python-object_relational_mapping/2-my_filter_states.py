#!/usr/bin/python3

"""
Lists all states with name matching the argument from
the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv


def main():
    db = MySQLdb.connect(
        host='localhost', user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states
                 WHERE BINARY name LIKE '{}'
                 ORDER BY states.id""".format(argv[4]))

    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    main()
