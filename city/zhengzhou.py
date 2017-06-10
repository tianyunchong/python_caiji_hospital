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
#  参数b=(12611382,4109971;12708790,4141395), 暂未确认具体作用，但是如果只不一样，可能会获取不到内容
#
url = 'http://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=after_baidu&pcevaname=pc4.1&qt=spot&' \
      'from=webmap&c=268&wd=医院&wd2=&pn=%s&nn=%s&db=0&sug=0&addr=0&pl_data_type=hospital&' \
      'pl_sub_type=医院&pl_price_section=0,+&pl_sort_type=&pl_sort_rule=0&' \
      'pl_discount2_section=0,+&pl_groupon_section=0,+&pl_cater_book_pc_section=0,+&' \
      'pl_hotel_book_pc_section=0,+&pl_ticket_book_flag_section=0,+&pl_movie_book_section=0,+&' \
      'pl_business_type=hospital&pl_business_id=&da_src=pcmappg.poi.page&on_gel=1&src=7&gr=3&l=12&rn=50&' \
      'tn=B_NORMAL_MAP&u_loc=12647350,4112147&ie=utf-8&b=(12611382,4109971;12708790,4141395)&t=1494678543176'



url = 'http://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=con&' \
      'from=webmap&c=268&wd=医院&wd2=&pn=%s&nn=%s&db=0&sug=0&addr=0&pl_data_type=hospital&' \
      'pl_sub_type=医院&pl_price_section=0,+&pl_sort_type=&pl_sort_rule=0&' \
      'pl_discount2_section=0,+&pl_groupon_section=0,+&pl_cater_book_pc_section=0,+&' \
      'pl_hotel_book_pc_section=0,+&pl_ticket_book_flag_section=0,+&pl_movie_book_section=0,+&' \
      'pl_business_type=hospital&pl_business_id=&da_src=pcmappg.poi.page&on_gel=1&src=7&gr=3&l=11&tn=B_NORMAL_MAP&' \
      'u_loc=12636816,4113919&ie=utf-8&b=(12561424,4054975;12748048,4121279)&t=1496988995469'
for i in range(0, 200):
    print "-----------第%s页----------------\n" % i
    realUrl =  url % (i, i * 10)
    response = urllib2.urlopen(realUrl)
    html = response.read()
    jsonStr = json.loads(html)
    query = session.query(Hospital)
    if "content" not in jsonStr:
        print realUrl
        continue
    for item in jsonStr["content"]:
        # for k, v in item.items():
        #     print k, "\t", v, "\n"
        # break
        if "name" not in item.keys():
            continue
        name = item["name"]
        if query.filter(Hospital.name == name).first():
            continue
        print name
        address = item["addr"] if "addr" in item.keys() else ""
        # 将医院的信息存储入库
        hospital = Hospital()
        hospital.name = name
        hospital.address = address
        session.add(hospital)
        session.commit()