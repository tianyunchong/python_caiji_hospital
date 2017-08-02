#!/bin/python2.7
# coding=utf-8
from models.baseModel import BaseModel
from sqlalchemy import Column
from sqlalchemy.types import CHAR, Integer, String, VARCHAR, Float, TEXT
from models.baseModel import session
"""
CREATE TABLE `dianpin_rel` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL COMMENT '医院名称',
  `searchtitle` varchar(255) DEFAULT NULL COMMENT '大众点评搜索的名称',
  `shopstar` int(11) DEFAULT NULL COMMENT '商户星级',
  `reviewcount` int(11) DEFAULT NULL COMMENT '评论数量',
  `tel` varchar(30) DEFAULT NULL COMMENT '电话',
  `avgprice` float DEFAULT NULL COMMENT '人均消费(单位元)',
  `address` varchar(255) DEFAULT NULL COMMENT '实际地址',
  `businesshour` varchar(50) DEFAULT NULL COMMENT '营业时间',
  `doctorscore` float DEFAULT NULL COMMENT '医生评分',
  `facilitiesscore` float DEFAULT NULL COMMENT '设施评分',
  `guahaoscore` float DEFAULT NULL COMMENT '挂号评分',
  `infofrom` varchar(100) DEFAULT NULL COMMENT '信息来源页面地址',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
class DianpinRel(BaseModel):
    __tablename__ = "dianpin_rel"

    #主键
    id = Column(Integer, primary_key=True)
    #医院名称
    title = Column(VARCHAR(255))
    #大众点评搜索的名称
    searchtitle = Column(VARCHAR(255))
    #商户星级
    shopstar = Column(Integer)
    #评论数量
    reviewcount = Column(Integer)
    #电话
    tel = Column(VARCHAR(30))
    #人均消费
    avgprice = Column(Float)
    #实际地址
    address = Column(VARCHAR(255))
    #营业时间
    businesshour = Column(VARCHAR(50))
    #医生评分
    doctorscore = Column(Float)
    #设施评分
    facilitiesscore = Column(Float)
    #挂号评分
    guahaoscore = Column(Float)
    #信息来源页面url
    infofrom = Column(VARCHAR(100))

    def commit(self):
        """
        提交下修改内容
        :return:
        """
        session.add(self)
        session.commit()
