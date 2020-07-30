import psycopg2
import sys
import json

"""connexion à la base de données
"""
def db_connexion(database):
    con = psycopg2.connect("dbname={} user={} host={} password={}" .format(
        database['db'],
        database['user'],
        database['host'],
        database['password']
    ))

    return con

"""requete envoyer à la base de données
"""
def query(sql, params, database):
    try:
        con = db_connexion(database)

        cur = con.cursor()
        cur.execute(sql, params)
        rows = cur.fetchall()
    except Exception as e:
        print(e)
    finally:
        if con:
            con.close()
    return rows

"""construction d'un dictionnaire
"""
def dict(sql, params, database):
    return query(sql, params, database)

"""retourner le resultat en format json
"""
def json_mode(query, params, database):
    return json.dumps(query(query, params, database))

"""recuperer un seul enregistrement
"""
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

"""inserer la ligne dans la base de données
"""
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

"""executer plusieurs requettes
"""
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
