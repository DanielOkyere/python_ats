#!/usr/bin/env python3

"""
Class: User
Description:
    Defines all properties and methods on User
"""
import models
from models.base import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5


class User(BaseModel, Base):
    """
    Defines the class declarations for user
    """
    __tablename__ = 'users'
    username = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """ Initializes a user object"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, key, value):
        """ Hashes the user password"""
        if key == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(key, value)
