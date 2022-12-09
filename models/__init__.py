#!/usr/bin/python3
"""
Initialize enitities

"""

from models.database.db import DBStorage
storage = DBStorage()

storage.reload()
