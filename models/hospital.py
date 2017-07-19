#!python.exe
# coding=utf-8
from sqlalchemy import Column
from sqlalchemy.types import CHAR, Integer, String, VARCHAR
from models.baseModel import BaseModel
from models.baseModel import session
import sys
'''
CREATE TABLE `hospital` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL COMMENT '医院名称',
  `address` varchar(255) DEFAULT NULL COMMENT '详细地址',
  `location` varchar(100) DEFAULT NULL COMMENT '经纬度',
  `telephone` varchar(50) DEFAULT NULL COMMENT '联系电话',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=397 DEFAULT CHARSET=utf8;
'''
class Hospital(BaseModel):
    __tablename__ = 'hospital'

    #主键id
    id = Column(Integer, primary_key=True)
    # 医院名称
    name = Column(VARCHAR(255))
    # 具体地址
    address = Column(VARCHAR(255))
    # 经纬度,json字符串
    location = Column(VARCHAR(100))
    # 电话
    telephone = Column(VARCHAR(50))

    def exist(self, name):
        '''check info is exist'''
        res = session.query(self.__class__).filter(self.__class__.name == name).first()
        if res:
            return res.id
        return False
