#!python.exe
# coding=utf-8
from sqlalchemy import Column
from sqlalchemy.types import CHAR, Integer, String, VARCHAR
from models.baseModel import BaseModel


class Hospital(BaseModel):

    __tablename__ = 'hospital'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255))
    address = Column(VARCHAR(255))