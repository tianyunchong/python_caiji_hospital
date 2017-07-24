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
from dazhongdianping.detail import Detail

id = 0
while 1:
    item = session.query(Hospital).filter(text('id > :id')).params(id=id).limit(1).all()
    if not item:
        break
    id = item[0].id
    name = item[0].name
    # 开始检索大众点评搜索页面，获取匹配的页面数据
    search_obj = Search(name)
    detail_url = search_obj.get_match_detail_url()
    if detail_url == "":
        continue
    # 提取大众点评详情页面的数据，并存入数据库
    detail_obj = Detail(detail_url)
    detail_base_info = detail_obj.get_base_detail()
