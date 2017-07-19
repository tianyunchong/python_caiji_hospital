#!/usr/bin/python2.7
#coding=utf-8
from models.baseModel import BaseModel
from sqlalchemy import Column
from sqlalchemy.types import CHAR, Integer, String, VARCHAR, Float, TEXT
from models.baseModel import session
import sys
'''
CREATE TABLE `baidu_rel` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `hostid` int(11) DEFAULT NULL COMMENT '医院信息id',
  `streetid` char(30) DEFAULT NULL COMMENT '街景图id',
  `poiuid` char(30) DEFAULT NULL COMMENT 'poi信息点唯一标识',
  `service_rating` float DEFAULT NULL COMMENT '服务评分',
  `comment_num` int(11) DEFAULT NULL COMMENT '评论数量',
  `price` float DEFAULT NULL COMMENT '商户价格',
  `image_num` int(11) DEFAULT NULL COMMENT '图片数量',
  `tag` varchar(50) DEFAULT NULL COMMENT '标签',
  `navi_location` varchar(255) DEFAULT NULL COMMENT '导航点坐标',
  `technology_rating` float DEFAULT NULL COMMENT '技术评分',
  `detail_url` varchar(100) DEFAULT NULL COMMENT 'poi详情页',
  `type` varchar(100) DEFAULT NULL COMMENT '所属分类',
  `shop_hours` varchar(255) DEFAULT NULL COMMENT '营业时间',
  `description` text COMMENT '信息描述',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=459 DEFAULT CHARSET=utf8;
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
    #服务评分
    service_rating = Column(Float)
    #评论数量
    comment_num = Column(Integer)
    #商户价格
    price = Column(Float)
    #图片数量
    image_num = Column(Integer)
    #标签
    tag = Column(VARCHAR(50))
    #导航点坐标
    navi_location = Column(VARCHAR(255))
    #技术评分
    technology_rating = Column(Float)
    #poi详情页地址
    detail_url = Column(VARCHAR(100))
    #所属分类
    type = Column(VARCHAR(100))
    #营业时间
    shop_hours = Column(VARCHAR(255))
    #信息描述
    description = Column(TEXT)

    '''
        根据医院id获取对应百度相关信息
        hostid  医院的id  
    '''
    def get_id_by_hostid(self, hostid):
        res = session.query(self.__class__).filter(self.__class__.hostid == hostid).first()
        if res:
            return res.id
        return False

