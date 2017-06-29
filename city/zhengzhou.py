#! python.exe
# coding=utf-8
import urllib2,urllib
import json
import sys,os
sys.path.append(os.path.dirname(os.getcwd()))
from models.hospital import Hospital
from models.baseModel import session
reload(sys)

sys.setdefaultencoding("utf-8")
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
    #print json.dumps(jsonStr, ensure_ascii=False, encoding="utf-8")
    for item in jsonStr["results"]:
        hospital = Hospital()
        if hospital.exist(item["name"]):
            continue
        # 将医院的信息存储入库
        print "%s is write to database" % item["name"]
        hospital.name = item["name"]
        hospital.address = item["address"]
        session.add(hospital)
        session.commit()