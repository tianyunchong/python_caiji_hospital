#!/bin/python2.7
# coding=utf-8
"""
提取大众点评详情页面的数据返回
"""
from library.http.http_base import HttpOp
import sys
from bs4 import BeautifulSoup
import re


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
            "shop_star" : 0,# 大众点评商户星级
            "reviewCount" : 0,#评论数量
            "avgPrice" : 0,#人均消费
            "comment_score" : {#评分
                "doctor" : 0,#医生评分
                "facilities" : 0,#设施评分
                "guahao" : 0,#挂号评分
            },
        }
        #选择器选择基本信息标签
        baseinfo = self.soup.select("#basic-info")[0]
        #获取星级
        baseinfo_star_class = baseinfo.select("div[class='brief-info']")[0].find("span").attrs["class"]
        if len(baseinfo_star_class) < 2:
            detail["shop_star"] = None
        else:
            match_star = re.findall(r"mid-str(.+)", baseinfo_star_class[1])
            if match_star:
                detail["shop_star"] = match_star[0]
        #获取评论数量
        baseinfo_review = baseinfo.select("#reviewCount")[0].text
        match_review = re.findall(r"(.+)条评论", baseinfo_review.encode("utf-8"))
        if match_review:
            detail["reviewCount"] = match_review[0]
        #获取人均消费
        baseinfo_avg = baseinfo.select("#avgPriceTitle")[0].text
        match_avg = re.findall(r"人均：\s?(\d+)元", baseinfo_avg.encode("utf-8"))
        if match_avg:
            detail["avgPrice"] = match_avg[0]
        #获取下评分数据
        baseinfo_comment = baseinfo.select("#comment_score")[0].findChildren()
        for item in baseinfo_comment:
            item_text = item.text
            #正则匹配下医生的评分
            
            #正则匹配获取下设施的评分
            #正则匹配获取下挂号的评分
        sys.exit()

    def get_content_html(self):
        """
        页面提取下内容
        :return:
        """
        #获取下cookie信息
        cookies = HttpOp.get_html_cookie("https://www.dianping.com/")
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding" : "gzip, deflate, br",
            "Accept-Language" : "zh-CN,zh;q=0.8",
            "Connection": "keep-alive",
            "Host" : "www.dianping.com",
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
        }
        self.html = HttpOp.get_html_data(self.url, headers=headers, cookies=cookies)
        self.soup = BeautifulSoup(self.html, "lxml")