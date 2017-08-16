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
from models.dianpinrelcomments import DianpinRelComments
from models.dianpinrelpictures import DianpinRelPictures
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
    detail_url_dict = search_obj.get_match_detail_url()
    if not detail_url_dict:
        print "######%s\t在大众点评中不存在##########" % name
        continue
    # 提取大众点评详情页面的数据，并存入数据库
    detail_obj = Detail(detail_url_dict["url"])
    detail_base_info = detail_obj.get_base_detail()
    detail_model = DianpinRel()
    detail_model.title = name
    detail_model.searchtitle = detail_url_dict["searchname"]
    detail_model.shopstar = detail_base_info["shop_star"]
    detail_model.reviewcount = detail_base_info["reviewCount"]
    detail_model.tel = detail_base_info["tel"]
    detail_model.avgprice = detail_base_info["avgPrice"]
    detail_model.address = detail_base_info["address"]
    detail_model.businesshour = detail_base_info["businessHour"].encode("utf-8")
    detail_model.doctorscore = detail_base_info["comment_score"]["doctor"]
    detail_model.facilitiesscore = detail_base_info["comment_score"]["facilities"]
    detail_model.guahaoscore = detail_base_info["comment_score"]["guahao"]
    detail_model.infofrom = detail_url_dict["url"]
    detail_model.commit()
    detail_model_id = detail_model.id
    # 提取大众点评评论信息,并存入数据库
    comment_obj = Comments(detail_url_dict["url"])
    comment_list = comment_obj.get_comments()
    # 循环存储下所有的评论信息
    for item in comment_list:
        detail_comments_model = DianpinRelComments()
        detail_comments_model.relid = detail_model_id
        detail_comments_model.username = item["username"].encode("utf-8")
        detail_comments_model.avatar = item["avatar"]
        detail_comments_model.level = item["level"]
        detail_comments_model.comments = item["detail"].encode("utf-8")
        detail_comments_model.commit()
    # 提取大众点评图片信息,并存入数据库
    pictureObj = Picture(detail_url_dict["url"])
    picture_list = pictureObj.get_picture()
    for item in picture_list:
        detail_picture_model = DianpinRelPictures()
        detail_picture_model.relid = detail_model_id
        detail_picture_model.uptimestr = item["uptimestr"].encode("utf-8")
        detail_picture_model.upuser = item["upuser"].encode("utf-8")
        detail_picture_model.thumbpic = item["thumb_pic"]
        detail_picture_model.bigpic = item["big_pic"]
        detail_picture_model.commit()


