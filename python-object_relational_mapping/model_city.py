#!/usr/bin/python3
"""Defines the City class linked to the MySQL table cities."""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Represents a city, mapped to the cities table."""
    __tablename__ = "cities"
    id = Column(Integer, unique=True, nullable=False,
                primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
