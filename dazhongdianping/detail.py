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
            "address" : "",#实际地址
            "tel" : "",#电话
            "businessHour" : "",#营业时间
            "comment_score" : {#评分
                "doctor" : 0,#医生评分
                "facilities" : 0,#设施评分
                "guahao" : 0,#挂号评分
            },
        }
        baseinfo_ele = self.soup.select("#basic-info")
        if not baseinfo_ele:
            return detail
        print self.url
        #选择器选择基本信息标签
        baseinfo = baseinfo_ele[0]
        #获取星级
        baseinfo_star_class = baseinfo.select("div[class='brief-info']")[0].find("span").attrs["class"]
        if len(baseinfo_star_class) < 2:
            detail["shop_star"] = None
        else:
            match_star = re.findall(r"mid-str(.+)", baseinfo_star_class[1])
            if match_star:
                detail["shop_star"] = match_star[0]
        #获取评论数量
        detail["reviewCount"] = self.get_base_detail_reviewcount(baseinfo)
        #获取人均消费
        detail["avgPrice"] = self.get_base_detail_avgprice(baseinfo)
        #获取下评分数据
        detail["comment_score"] = self.get_base_detail_commentscore(baseinfo)
        #获取下实际地址
        match_addres = baseinfo.find("span", itemprop="street-address")
        if match_addres:
            detail["address"] =  match_addres.text.strip()
        #获取下电话号码
        match_tel = baseinfo.find("span", itemprop="tel")
        if match_tel:
            detail["tel"] = match_tel.text.strip()
        #获取其他信息数组
        detail["businessHour"] = self.get_base_detail_businesshour(baseinfo)
        return detail

    def get_base_detail_businesshour(self, baseinfo):
        """
        获取下营业时间
        :param baseinfo:
        :return:
        """
        match_other = baseinfo.find("div", class_=["other", "J-other"])
        match_other_children = match_other.findChildren("p") if match_other else None
        if not match_other_children:
            return ""
        for item in match_other_children:
            item_children = item.findChildren("span")
            if len(item_children) < 2:
                continue
            if item_children[0].text == u"营业时间：":
                return  item_children[1].text.strip()
        return ""

    def get_base_detail_avgprice(self, baseinfo):
        """
        获取下人均消费
        :param baseinfo:
        :return:
        """
        baseinfo_avg_ele = baseinfo.select("#avgPriceTitle")
        if not baseinfo_avg_ele:
            return 0
        baseinfo_avg = baseinfo_avg_ele[0].text
        match_avg = re.findall(r"人均：\s?(\d+)元", baseinfo_avg.encode("utf-8"))
        if match_avg:
            return match_avg[0]
        return 0

    def get_base_detail_reviewcount(self, baseinfo):
        """
        获取下评论数量
        :param baseinfo:
        :return:
        """
        baseinfo_review_ele = baseinfo.select("#reviewCount")
        if not baseinfo_review_ele:
            return 0
        baseinfo_review = baseinfo_review_ele[0].text
        match_review = re.findall(r"(.+)条评论", baseinfo_review.encode("utf-8"))
        if match_review:
            return match_review[0]
        return 0


    def get_base_detail_commentscore(self, baseinfo):
        """
        获取评分数据信息
        :param baseinfo:
        :return:
        """
        comment_info = {"doctor":0, "facilities":0, "guahao":0}
        baseinfo_comment_ele = baseinfo.select("#comment_score")
        if len(baseinfo_comment_ele) < 1:
            return comment_info
        baseinfo_comment = baseinfo_comment_ele[0].findChildren("span")
        for item in baseinfo_comment:
            item_text = item.text
            match_avg = re.findall(r"(医生|设施|挂号)：([\d\.]+)", item_text.encode("utf-8"))
            if match_avg and match_avg[0][0].encode("utf-8") == "医生":
                comment_info["doctor"] = match_avg[0][1]
            elif match_avg and match_avg[0][0].encode("utf-8") == "设施":
                comment_info["facilities"] = match_avg[0][1]
            elif match_avg and match_avg[0][0].encode("utf-8") == "挂号":
                comment_info["guahao"] = match_avg[0][1]
        return comment_info

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