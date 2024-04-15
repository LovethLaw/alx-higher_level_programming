#!/usr/bin/python3
"""my module on MySQLdb"""
import MySQLdb
import sys
if __name__ == "__main__":

    args = sys.argv
    user = args[1]
    password = args[2]
    database = args[3]
    user_arg = args[4]

    db = MySQLdb.connect(host='localhost', user=user,
                         password=password, port=3306, database=database)

    cur = db.cursor()
    query = """SELECT cities.name FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name LIKE %s
    ORDER BY states.id"""
    cur.execute(query, (user_arg,))
    result = cur.fetchall()
    val = ''
    for res in result:
        val += f'{res[0]}, '
    val = val.rstrip(', ')
    # val = val[:-2]
    print(val)
    cur.close()
    db.close()
