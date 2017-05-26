#! python
# coding=utf-8

import sys,os,urllib
sys.path.append(os.path.dirname(os.getcwd()))
url = 'http://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=after_baidu&pcevaname=pc4.1&qt=spot' \
      '&from=webmap&c=268&wd=医院&wd2=&pn=%s&nn=%s&db=0&sug=0&addr=0&pl_data_type=hospital&pl_sub_type=医院&' \
      'pl_price_section=0,+&pl_sort_type=&pl_sort_rule=0&pl_discount2_section=0,+&pl_groupon_section=0,+&' \
      'pl_cater_book_pc_section=0,+&pl_hotel_book_pc_section=0,+&pl_ticket_book_flag_section=0,+&pl_movie_book_section=0,+&' \
      'pl_business_type=hospital&pl_business_id=&da_src=pcmappg.poi.page&on_gel=1&src=7&gr=3&l=12&rn=50&tn=B_NORMAL_MAP&' \
      'u_loc=12647350,4112147&ie=utf-8&b=(12611382,4109971;12708790,4141395)&t=1494678543176'
print url % (1, 1 * 10)