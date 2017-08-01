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
from dazhongdianping.comments import Comments
from dazhongdianping.pictures import Picture
from models.dianpinrel import DianpinRel
id = 0
while 1:
    item = session.query(Hospital).filter(text('id > :id')).params(id=id).limit(1).all()
    if not item:
        break
    id = item[0].id
    name = item[0].name
    print "开始抓取<%s>的大众点评信息" % name
    # 开始检索大众点评搜索页面，获取匹配的页面数据
    search_obj = Search(name)
    detail_url = search_obj.get_match_detail_url()
    if detail_url == "":
        print "######%s在大众点评中不存在##########" % name
        continue
    # 提取大众点评详情页面的数据，并存入数据库
    detail_obj = Detail(detail_url)
    detail_base_info = detail_obj.get_base_detail()
    detail_model = DianpinRel()
    detail_model.shopstar = detail_base_info["shop_star"]
    detail_model.reviewcount = detail_base_info["reviewCount"]
    detail_model.tel = detail_base_info["tel"]
    detail_model.avgprice = detail_base_info["avgPrice"]
    detail_model.address = detail_base_info["address"]
    detail_model.businesshour = detail_base_info["businessHour"].encode("utf-8")
    detail_model.doctorscore = detail_base_info["comment_score"]["doctor"]
    detail_model.facilitiesscore = detail_base_info["comment_score"]["facilities"]
    detail_model.guahaoscore = detail_base_info["comment_score"]["guahao"]
    detail_model.infofrom = detail_url
    detail_model.commit()
    # 提取大众点评评论信息,并存入数据库
    # comment_obj = Comments(detail_url)
    # comment_list = comment_obj.get_comments()
    # 提取大众点评图片信息,并存入数据库
    #pictureObj = Picture(detail_url)
    #picture_list = pictureObj.get_picture()
    #sys.exit()
