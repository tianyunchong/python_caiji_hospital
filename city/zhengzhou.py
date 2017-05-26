#! python.exe
# coding=utf-8
import urllib2
import json
import sys,os
sys.path.append(os.path.dirname(os.getcwd()))
from models.hospital import Hospital
from models.baseModel import session
reload(sys)

sys.setdefaultencoding("utf-8")
url = 'http://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=after_baidu&pcevaname=pc4.1&qt=spot&' \
      'from=webmap&c=268&wd=%E5%8C%BB%E9%99%A2&wd2=&pn=0&nn=0&db=0&sug=0&addr=0&pl_data_type=hospital&' \
      'pl_sub_type=%E5%8C%BB%E9%99%A2&pl_price_section=0%2C%2B&pl_sort_type=&pl_sort_rule=0&' \
      'pl_discount2_section=0%2C%2B&pl_groupon_section=0%2C%2B&pl_cater_book_pc_section=0%2C%2B&' \
      'pl_hotel_book_pc_section=0%2C%2B&pl_ticket_book_flag_section=0%2C%2B&pl_movie_book_section=0%2C%2B&' \
      'pl_business_type=hospital&pl_business_id=&da_src=pcmappg.poi.page&on_gel=1&src=7&gr=3&l=12&rn=50&' \
      'tn=B_NORMAL_MAP&u_loc=12647350,4112147&ie=utf-8&b=(12611382,4109971;12708790,4141395)&t=1494678543176'

response = urllib2.urlopen(url)
html = response.read()
jsonStr = json.loads(html)
query = session.query(Hospital)
for item in jsonStr["content"]:
    # for k, v in item.items():
    #     print k, "\t", v, "\n"
    # break
    if "name" not in item.keys():
        continue
    name = item["name"]
    print name
    if query.filter(Hospital.name == name).first():
        continue
    address = item["addr"] if "addr" in item.keys() else ""
    # 将医院的信息存储入库
    hospital = Hospital()
    hospital.name = name
    hospital.address = address
    session.add(hospital)
    session.commit()
