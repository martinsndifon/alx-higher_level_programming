#!/usr/bin/python3

"""Lists all states with name starting with 'N' from the database
hbtn_0e_0_usa"""

import MySQLdb
from sys import argv


def main():
    """The query below could also be written as
    ...name LIKE BINARY UPPER('N%')..."""

    db = MySQLdb.connect(
        host='localhost', user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states
                 WHERE BINARY name LIKE UPPER('N%')
                 ORDER BY states.id""")

    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    main()
