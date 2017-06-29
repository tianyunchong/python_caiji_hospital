#!python.exe
# coding=utf-8
from sqlalchemy import Column
from sqlalchemy.types import CHAR, Integer, String, VARCHAR
from models.baseModel import BaseModel
from models.baseModel import session


class Hospital(BaseModel):
    __tablename__ = 'hospital'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255))
    address = Column(VARCHAR(255))

    def exist(self, name):
        '''check info is exist'''
        res = session.query(self.__class__).filter(self.__class__.name == name).first()
        if res:
            return True
        return False
