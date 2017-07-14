#! python.exe
# coding=utf-8
import urllib2,urllib
import json
import sys,os
sys.path.append(os.path.dirname(os.getcwd()))
from models.hospital import Hospital
from models.baseModel import session
from models.baidurel import BaiduRel
reload(sys)
sys.setdefaultencoding("utf-8")

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
    baiduRelObj.hostid = baidu_id
    baiduRelObj.streetid = item["street_id"] if item.has_key("street_id") else ""
    baiduRelObj.poiuid   = item["uid"]
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
    session.add(hospital)
    session.commit()
    return hospital.id

#
#  http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-placeapi
#
baiduKey = "1281fa2a4b458eb45252c8ff79bc5ef8"
url = 'http://api.map.baidu.com/place/v2/search?q=医院&region=郑州&output=json&ak=%s&page_size=%s&page_num=%s'
print url
for i in range(0, 200):
    print "-----------第%s页----------------\n" % (i+1)
    realUrl = url % (baiduKey, 10, i)
    response = urllib2.urlopen(realUrl)
    html = response.read()
    jsonStr = json.loads(html)
    if jsonStr["status"] != 0:
        continue
    #result is empty, break
    if not jsonStr["results"]:
        break
    for item in jsonStr["results"]:
        baidu_id = insert_hospital(item)
        insert_baidu_rel(baidu_id, item)


