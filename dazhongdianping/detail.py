#!/bin/python2.7
# coding=utf-8
"""
提取大众点评详情页面的数据返回
"""
from library.http.http_base import HttpOp
import sys
from bs4 import BeautifulSoup


class Detail(object):
    # 需要获取的详情页面url
    url = None
    # 提取到的详情页面内容
    html = None
    # 初始化下beautifysoup对象
    soup = None

    def __init__(self, url):
        """
        初始化
        :param url:
        :return:
        """
        self.url = url
        self.get_content_html()

    def get_base_detail(self):
        """
        获取下基本信息
        :return:
        """
        detail = {
            "shop_star" : None,# 大众点评商户星级
            "reviewCount" : 0,#评论数量
            "avgPrice" : 0,#人均消费
            "comment_score" : {#评分
                "doctor" : 0,#医生评分
                "facilities" : 0,#设施评分
                "guahao" : 0,#挂号评分
            },
        }
        #选择器选择基本信息标签
        print self.soup
        baseinfo = self.soup.select("#basic-info")
        print type(baseinfo)
        print baseinfo
        sys.exit()
        #获取星级
        baseinfo_star = baseinfo.find_all("div[class='brief-info']").childern
        print baseinfo_star
        sys.exit()

    def get_content_html(self):
        """
        页面提取下内容
        :return:
        """
        #获取下cookie信息
        HttpOp.get_html_cookie("https://www.dianping.com/")
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding" : "gzip, deflate, br",
            "Accept-Language" : "zh-CN,zh;q=0.8",
            "Connection": "keep-alive",
            "Host" : "www.dianping.com",
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
        }
        self.html = HttpOp.get_html_data(self.url, headers=headers)
        sys.exit()
        self.soup = BeautifulSoup(self.html, "lxml")