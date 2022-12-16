#!/usr/bin/python3

"""
Module for database tests
"""
import unittest
import MySQLdb
from models.user import User
from models import storage
from datetime import datetime
from random import random
import os


class TestDBStorage(unittest.TestCase):
    """Testing dbstorage engine"""
    def test_new_and_save(self):
        """Testing save and new methods"""
        db = MySQLdb.connect(user=os.getenv('ATS_DB_USER'),
                             host=os.getenv('ATS_DB_HOST'),
                             passwd=os.getenv('ATS_DB_PWD'),
                             port=3306,
                             db=os.getenv('ATS_DB_NAME'))
        
        new_user = User(**{'username': 'daniel',
                           'password': '123456789',
                           'email':'daniel@gmail.com'})
        
        cur = db.cursor()
        cur.execute('SELECT COUNT(*) FROM user')
        old_count = cur.fetchall()
        cur.close()
        db.close()
        new_user.save()
        db = MySQLdb.connect(user=os.getenv('ATS_DB_USER'),
                             host=os.getenv('ATS_DB_HOST'),
                             passwd=os.getenv('ATS_DB_PWD'),
                             port=3306,
                             db=os.getenv('ATS_DB_NAME'))
        cur = db.cursor()
        cur.execute('SELECT COUNT(*) FROM user')
        new_count = cur.fetchall()
        self.assertEqual(new_count[0][0], old_count[0][0] + 1)
        cur.close()
        db.close()
        
    def test_new(self):
        """New object is correctly added to database"""
        new = User(
            username="daniel.okyere",
            password='password',
            email='daniel.okyere@mail.com'
        )
        self.assertFalse(new in storage.all().values())
        new.save()
        self.assertTrue(new in storage.all().values())
        dbc = MySQLdb.connect(user=os.getenv('ATS_DB_USER'),
                             host=os.getenv('ATS_DB_HOST'),
                             passwd=os.getenv('ATS_DB_PWD'),
                             port=3306,
                             db=os.getenv('ATS_DB_NAME'))
        cur = dbc.cursor()
        cur.execute(f"SELECT * FROM user WHERE id='{new.id}'")
        result = cur.fetchone()
        self.assertTrue(result is not None)
        self.assertIn('daniel.okyere@mail.com', result)
        self.assertIn(str(new.password), result)
        self.assertIn('daniel.okyere', result)
        cur.close()
        dbc.close()
        
    def test_delete(self):
        """Test if object is deleted"""
        new = User(
            username="jackfrost",
            password='password',
            email='jackfrost@mail.com'
        )
        obj_key = 'User.{}'.format(new.id)
        dbc = MySQLdb.connect(user=os.getenv('ATS_DB_USER'),
                             host=os.getenv('ATS_DB_HOST'),
                             passwd=os.getenv('ATS_DB_PWD'),
                             port=3306,
                             db=os.getenv('ATS_DB_NAME'))
        new.save()
        self.assertTrue(new in storage.all().values())
        cur = dbc.cursor()
        cur.execute(f"SELECT * FROM user WHERE id='{new.id}'")
        result = cur.fetchone()
        self.assertTrue(result is not None)
        self.assertIn('jackfrost', result)
        self.assertIn(str(new.password), result)
        self.assertIn('jackfrost@mail.com', result)
        self.assertIn(obj_key, storage.all(User).keys())
        new.delete()
        self.assertNotIn(obj_key, storage.all(User).keys())
        cur.close()
        dbc.close()
        
    def test_reload(self):
        """ Test reloading of database session """
        dbc = MySQLdb.connect(user=os.getenv('ATS_DB_USER'),
                             host=os.getenv('ATS_DB_HOST'),
                             passwd=os.getenv('ATS_DB_PWD'),
                             port=3306,
                             db=os.getenv('ATS_DB_NAME'))
        cur = dbc.cursor()
        user_id = random()
        cur.execute(
            'INSERT INTO user(id, created_at, updated_at, username, password, email)' +
            ' VALUES(%s, %s, %s, %s, %s, %s);',
            [
                '{}-by-me'.format(user_id),
                str(datetime.now()),
                str(datetime.now()),
                'username',
                'password',
                'username@mail.com',
            ]
        )
        self.assertNotIn('User.{}-by-me'.format(user_id), storage.all())
        dbc.commit()
        storage.reload()
        self.assertIn('User.{}-by-me'.format(user_id), storage.all())
        cur.close()
        dbc.close