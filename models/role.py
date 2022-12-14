#!/usr/bin/python3

"""
Class Role

Description:
    Defines all properties and method on Role
"""
import models
from models.base import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, JSON


class Role(BaseModel, Base):
    """
    Defines the class for roles
    """
    __tablename__ = 'roles'
    name = Column(String(128), nullable=False)
    permissions = Column(JSON)


    def __init__(self, *args, **kwargs):
        """initializes a role object"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, key, value):
        """Set attributes"""
        super().__setattr__(key, value)