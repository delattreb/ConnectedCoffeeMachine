"""
Main.py
Auteur: Bruno DELATTRE
Date : 07/08/2016
"""

import unittest

from ..lib import com_mysql

class TestMySQL(unittest.TestCase):
    def test_select(self):
        com_mysql.req_insert(99999)
        id = com_mysql.req_select(99999)
        self.assertEqual(id, 99999)
        com_mysql.req_delete(99999)

    def test_insert(self):
        com_mysql.req_insert(99999)
        id = com_mysql.req_select(99999)
        self.assertEqual(id, 99999)
        com_mysql.req_delete(99999)

    def test_delete(self):
        com_mysql.req_delete(99999)
        id = com_mysql.req_select(99999)
        self.assertEqual(id, 0)


if __name__ == '__main__':
    unittest.main()
