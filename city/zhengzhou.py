#! python.exe
# coding=utf-8
import urllib2,urllib
import json
import sys,os
sys.path.append(os.path.dirname(os.getcwd()))
from models.hospital import Hospital
from models.baseModel import session
from models.baidurel import BaiduRel
from library.http.http_base import HttpOp
reload(sys)
sys.setdefaultencoding("utf-8")

'''
获取下poi详情页信息
'''
def get_poi_detail(poi_uid):
    defail_url = 'http://api.map.baidu.com/place/v2/detail?uid=%s&output=json&scope=2&ak=%s' % (poi_uid, baidu_key)
    html = HttpOp.get_html_data(defail_url)
    defail_json = json.loads(html)
    defail_info =  defail_json["result"] if defail_json.has_key("result") else None
    if not defail_info:
        return None
    defail_item = defail_info["detail_info"] if defail_info.has_key("detail_info") else None
    return defail_item

'''
增加百度相关信息
baiduid 医院信息主键id
item 获取的医院基本信息
'''
def insert_baidu_rel(baidu_id, item):
    baiduRelObj = BaiduRel()
    id = baiduRelObj.get_id_by_hostid(baidu_id)
    if id:
        return 0
    detail_dict = get_poi_detail(item["uid"])
    baiduRelObj.hostid = baidu_id
    baiduRelObj.streetid = item["street_id"] if item.has_key("street_id") else ""
    baiduRelObj.poiuid   = item["uid"]
    baiduRelObj.service_rating = detail_dict["service_rating"]
    baiduRelObj.comment_num = detail_dict["comment_num"]
    baiduRelObj.price = detail_dict["price"]
    baiduRelObj.image_num = detail_dict["image_num"]
    baiduRelObj.tag = detail_dict["tag"]
    baiduRelObj.navi_location = json.dumps(detail_dict["navi_location"], encoding="UTF-8") if detail_dict.has_key("navi_location") else ""
    baiduRelObj.technology_rating = detail_dict["technology_rating"]
    baiduRelObj.detail_url = detail_dict["detail_url"]
    baiduRelObj.type = detail_dict["type"]
    baiduRelObj.shop_hours = detail_dict["shop_hours"] if detail_dict.has_key("shop_hours") else ""
    baiduRelObj.description = detail_dict["description"] if detail_dict.has_key("description") else ""
    session.add(baiduRelObj)
    session.commit()
'''
增加医院记录信息
'''
def insert_hospital(item):
    hospital = Hospital()
    id = hospital.exist(item["name"])
    if id:
        return id
    print "%s is write to database" % item["name"]
    hospital.name = item["name"]
    hospital.address = item["address"]
    hospital.location = json.dumps(item["location"], encoding="utf-8")
    hospital.telephone = item["telephone"] if item.has_key("telephone") else ""
    session.add(hospital)
    session.commit()
    return hospital.id

#
#  http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-placeapi
#
baidu_key = "1281fa2a4b458eb45252c8ff79bc5ef8"
url = 'http://api.map.baidu.com/place/v2/search?q=医院&region=郑州&output=json&ak=%s&page_size=%s&page_num=%s'
print url
for i in range(0, 200):
    print "-----------第%s页----------------\n" % (i+1)
    realUrl = url % (baidu_key, 10, i)
    html = HttpOp.get_html_data(realUrl)
    jsonStr = json.loads(html)
    if jsonStr["status"] != 0:
        continue
    #result is empty, break
    if not jsonStr["results"]:
        break
    for item in jsonStr["results"]:
        baidu_id = insert_hospital(item)
        insert_baidu_rel(baidu_id, item)


