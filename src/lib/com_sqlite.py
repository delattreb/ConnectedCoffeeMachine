"""
Auteur: Bruno DELATTRE
Date : 07/08/2016
"""

import sqlite3

from lib import com_config


class SQLite:
    def __init__(self):
        self.connection, self.cursor = self.connect()

    def __del__(self):
        self.connection.close()

    def connect(self):
        config = com_config.getConfig()
        con = sqlite3.connect(config['SQLITE']['database'])
        cursor = con.cursor()
        return con, cursor

    def select(self, val):
        rows = self.cursor.execute("SELECT id FROM data WHERE id='" + str(val) + "'")
        id = 0
        for row in rows:
            id = row[0]
        return id

    def insert(self, val):
        try:
            self.cursor.execute("INSERT INTO data(id) VALUES('" + str(val) + "')")
            self.connection.commit()
        except:
            self.connection.rollback()

    def delete(self, val):
        try:
            self.cursor.execute("DELETE FROM data WHERE id ='" + str(val) + "'")
            self.connection.commit()
        except:
            self.connection.rollback()
