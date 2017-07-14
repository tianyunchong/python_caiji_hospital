#!/usr/bin/python2.7
#coding=utf-8
from models.baseModel import BaseModel
from sqlalchemy import Column
from sqlalchemy.types import CHAR, Integer, String, VARCHAR
from models.baseModel import session
import sys
'''
CREATE TABLE `baidu_rel` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `hostid` int(11) DEFAULT NULL COMMENT '医院信息id',
  `streetid` char(30) DEFAULT NULL COMMENT '街景图id',
  `poiuid` char(30) DEFAULT NULL COMMENT 'poi信息点唯一标识',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=437 DEFAULT CHARSET=utf8;
'''
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

