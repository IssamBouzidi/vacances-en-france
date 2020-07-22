import psycopg2
import sys
import json


def db_connexion(database):
    con = psycopg2.connect("dbname={} user={} host={} password={}" .format(
        database['db'],
        database['user'],
        database['host'],
        database['password']
    ))

    return con


def query(query, params, database):
    try:
        con = db_connexion(database)

        cur = con.cursor()
        cur.execute(query, params)
        rows = cur.fetchall()
    except Exception as e:
        print(e)
    finally:
        if con:
            con.close()
    return rows


def dict_mode(query, params, database):
    return query(query, params, database)


def json_mode(query, params, database):
    return json.dumps(query(query, params, database))


def scalar(query, params, database):
    try:
        con = db_connexion(database)

        cur = con.cursor()
        cur.execute(query, params)
        rows = cur.fetchone()[0]
    except Exception as e:
        print(e)
    finally:
        if con:
            con.close()
    return rows


def empty(query, params, database):
    last_id = None
    row_count = None
    try:
        con = db_connexion(database)

        cur = con.cursor()
        cur.execute(query, params)
        last_id = cur.lastrowid
        row_count = cur.rowcount
        con.commit()
    except Exception as e:
        print(e)
        pass
    finally:
        if con:
            con.close()
    return last_id, row_count


def transaction(queries, database):
    result = []
    try:
        con = db_connexion(database)
        cur = con.cursor()
        for query in queries:
            print(query)
            sql, params = query
            cur.execute(sql, params)
            result.append((cur.lastrowid, cur.rowcount))
        con.commit()
    except Exception as e:
        print(e)
        if con:
            con.rollback()
    finally:
        if con:
            con.close()

    return result
