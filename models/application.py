#!/usr/bin/python3

"""
Class application
Description:
    Defines all properties on application
"""
import models
from models.base import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Float


class Applications(BaseModel, Base):
    """
    Defines the class declaration for Applications
    """
    __tablename__ = 'applications'
    job_desc = Column(String(1000))
    resume = Column(String(1000))
    hard_skills = Column(Float)
    soft_skills = Column(Float)
    gen_skills = Column(Float)
    response = Column(String(10))
    company_name = Column(String(50))

    def __int__(self, *args, **kwargs):
        """ Initializes a user object"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, key, value):
        """ Sets attributes"""
        super().__setattr__(key, value)
