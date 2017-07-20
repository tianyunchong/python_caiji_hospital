#! /usr/bin/python2.7
# coding=utf-8
"""
大众点评数据采集主入口页面
"""
import sys, os

reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(os.path.dirname(os.getcwd()))
from models.baseModel import session
from models.hospital import Hospital
from sqlalchemy import text
from dazhongdianping.search import Search

id = 0
while 1:
    item = session.query(Hospital).filter(text('id > :id')).params(id=id).limit(1).all()
    if not item:
        break
    id = item[0].id
    name = item[0].name
    # 开始检索大众点评搜索页面，获取匹配的页面数据
    search_obj = Search(name)
    search_obj.get_match_detail_url()
