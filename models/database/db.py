#!/usr/bin/python3

"""
DB Storage Class
Description:
    Describes all the methods for handling database
    details
"""

from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from models.user import User
from models.base import BaseModel, Base
from models.application import Applications
from models.role import Role
import models

classes = {"User": User,
           "Role": Role,
           "Applications": Applications
           }

class DBStorage:
    """
    Class: DBStorage
    Description:
        Creates a db session

    Methods:
        all - query on all entities in the database
        new - creates a new entity and adds to session
        save - persists data to database
        delete - deletes data from database
        reload - reloads to have updated data in database
    """
    __session = None
    __engine = None

    def __init__(self):
        """
        Instantiates a DB Storage object
        """
        ATS_DB_USER = getenv('ATS_DB_USER')
        ATS_DB_PWD = getenv('ATS_DB_PWD')
        ATS_DB_HOST = getenv('ATS_DB_HOST')
        ATS_DB_NAME = getenv('ATS_DB_NAME')
        ATS_ENV = getenv('ATS_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(ATS_DB_USER,
                                             ATS_DB_PWD,
                                             ATS_DB_HOST,
                                             ATS_DB_NAME))

        if ATS_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on current database for class
        Args:
            cls: name of class
        Return:
            dictionary of class
        """
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj

        return (new_dict)

    def new(self, obj):
        """Adds all"""
        self.__session.add(obj)

    def save(self):
        """Commits all data changes to current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reloads all data from database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """ Returns the object based on the class name and its ID,
        or None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for v in all_cls.values():
            if v.id == id:
                return v

        return None

    def count(self, cls=None):
        """Count the number of objects in storage"""
        all_clss = classes.values()
        if not cls:
            count = 0
            for clas in all_clss:
                count += len(models.storage.all(cls).values())
        else:
            count = len(models.storage.all(cls).values())

        return count

