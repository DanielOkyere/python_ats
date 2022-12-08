#!/usr/bin/python3
"""
Initialize enitities

"""

from database.db import DBStorage
storage = DBStorage()

storage.reload()
