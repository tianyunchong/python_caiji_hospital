#!/bin/python2.7
# coding=utf-8
"""
存储大众点评详情页的评论信息
"""
from models.baseModel import BaseModel
from sqlalchemy import Column
from sqlalchemy.types import CHAR, Integer, String, VARCHAR, Float, TEXT
from models.baseModel import session
"""
CREATE TABLE `dianpin_rel_comments` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `relid` int(11) DEFAULT NULL COMMENT '大众点评详情信息id',
  `username` varchar(100) DEFAULT NULL COMMENT '评论用户名',
  `avatar` varchar(255) DEFAULT NULL COMMENT '评论用户的头像',
  `level` float DEFAULT NULL COMMENT '评论星级',
  `comments` text CHARACTER SET utf8mb4 COMMENT '评论的内容',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
"""
class DianpinRelComments(BaseModel):
    __tablename__ = "dianpin_rel_comments"

    #主键
    id = Column(Integer, primary_key=True)
    #大众点评详情页主键id
    relid = Column(Integer)
    #评论用户名
    username = Column(VARCHAR(100))
    #评论用户的头像地址
    avatar = Column(VARCHAR(255))
    #评论的星级
    level = Column(Float)
    #评论的具体内容
    comments = Column(TEXT)

    def commit(self):
        """
        提交下修改内容
        :return:
        """
        session.add(self)
        session.commit()