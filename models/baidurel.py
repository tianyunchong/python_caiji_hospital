#!/usr/bin/python2.7
#coding=utf-8
from models.baseModel import BaseModel
from sqlalchemy import Column
from sqlalchemy.types import CHAR, Integer, String, VARCHAR
from models.baseModel import session
import sys

class BaiduRel(BaseModel):
    __tablename__ = "baidu_rel"

    # 主键id
    id = Column(Integer, primary_key=True)
    # 医院信息id
    hostid = Column(Integer)
    # 百度街景图id
    streetid = Column(VARCHAR(30))
    # 百度poi信息点唯一标识
    poiuid = Column(VARCHAR(30))

    '''
        根据医院id获取对应百度相关信息
        hostid  医院的id  
    '''
    def get_id_by_hostid(self, hostid):
        res = session.query(self.__class__).filter(self.__class__.hostid == hostid).first()
        if res:
            return res.id
        return False

