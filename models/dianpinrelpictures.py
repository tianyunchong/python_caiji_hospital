#!/bin/python2.7
# coding=utf-8
"""
存储大众点评上传的图片
"""
from models.baseModel import BaseModel
from sqlalchemy import Column
from sqlalchemy.types import CHAR, Integer, String, VARCHAR, Float, TEXT
from models.baseModel import session
"""
CREATE TABLE `dianpin_rel_pictures` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `relid` int(11) DEFAULT NULL COMMENT '大众点评详情id',
  `uptimestr` varchar(100) DEFAULT NULL COMMENT '上传时间字符串',
  `upuser` varchar(100) DEFAULT NULL COMMENT '上传人员',
  `thumbpic` varchar(255) DEFAULT NULL COMMENT '上传的缩略图',
  `bigpic` varchar(255) DEFAULT NULL COMMENT '上传的大图',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=112 DEFAULT CHARSET=utf8;
"""
class DianpinRelPictures(BaseModel):
    __tablename__ = "dianpin_rel_pictures"
    #主键id
    id = Column(Integer, primary_key=True)
    #大众点评主键id
    relid = Column(Integer)
    #上传时间字符串
    uptimestr = Column(VARCHAR(100))
    #上传人员用户名
    upuser = Column(VARCHAR(100))
    #上传的缩略图
    thumbpic = Column(VARCHAR(255))
    #上传的大图
    bigpic = Column(VARCHAR(255))

    def commit(self):
        """
        提交下修改内容
        :return:
        """
        session.add(self)
        session.commit()

