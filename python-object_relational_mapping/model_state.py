#!/usr/bin/python3
"""Defines the State class linked to the MySQL table states."""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Represents a state, mapped to the states table."""
    __tablename__ = "states"
    id = Column(Integer, unique=True, nullable=False,
                primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
