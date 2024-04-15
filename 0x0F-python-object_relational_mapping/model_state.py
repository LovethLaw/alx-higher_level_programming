#!/usr/bin/python3
""" python file that contains the class
definition of a State and an instance Base
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """_summary_

    Args:
        Base (_type_): _description_
    """
    __tablename__ = "states"
    id = Column('id', Integer, autoincrement=True, primary_key=True)
    name = Column('name', String(128))
