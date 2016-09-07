"""
Main.py
Auteur: Bruno DELATTRE
Date : 07/08/2016
"""

import pymysql

from lib import com_config


def connect():
    config = com_config.getConfig()
    db = pymysql.connect(host=config['MYSQL']['host'], user=config['MYSQL']['user'], passwd=config['MYSQL']['password'],
                         db=config['MYSQL']['db'])
    cur = db.cursor()
    return cur, db


def req_select(val):
    cur, db = connect()
    cur.execute("SELECT id FROM data WHERE id='" + str(val) + "'")
    id = 0
    for row in cur.fetchall():
        id = row[0]
    db.close()
    return id


def req_insert(val):
    cur, db = connect()
    try:
        cur.execute("INSERT INTO data VALUES ('" + str(val) + "')")
        db.commit()
    except:
        db.rollback()
    db.close()


def req_delete(val):
    cur, db = connect()
    try:
        cur.execute("DELETE FROM data WHERE id= ('" + str(val) + "')")
        db.commit()
    except:
        db.rollback()
    db.close()
