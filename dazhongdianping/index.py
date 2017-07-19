#! /usr/bin/python2.7
# coding=utf-8
"""
大众点评数据采集主入口页面
"""
import sys,os
sys.path.append(os.path.dirname(os.getcwd()))
from models.baseModel import session
from models.hospital import Hospital
from sqlalchemy import text
id = 0
while 1:
    item = session.query(Hospital).filter(text('id > :id')).params(id=id).limit(1).all()
    if not item:
        break
    id = item[0].id
    print item[0].name
