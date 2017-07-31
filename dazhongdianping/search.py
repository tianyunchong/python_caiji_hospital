#!/bin/python2.7
# coding=utf-8
from library.http.http_base import HttpOp
import sys,urllib2
from bs4 import BeautifulSoup

class Search(object):
    # 要检索的关键词
    keyword = None
    # 要检索的搜索页面
    url = None
    # 要检索的搜索页面的html内容
    html = None

    def __init__(self, keyword):
        """
        初始化采集的url地址
        :param keyword:
        """
        self.keyword = keyword
        self.url = "https://www.dianping.com/search/keyword/160/0_%s" % urllib2.quote(keyword.encode("utf-8"))

    def get_match_detail_url(self):
        """
        获取匹配的页面详情页地址
        :return:
        """
        self.get_search_html()
        #解析html获取下内容
        soup = BeautifulSoup(self.html, "lxml")
        match_html_search = soup.select("div[id='shop-all-list']")
        if not match_html_search:
            return ""
        match_html = match_html_search[0]
        # 提取所有的所有结果，获取标题完全一致的搜索结果
        li_list = match_html.find_all("li")
        match_keyword = self.keyword.replace("-", "")
        for item in li_list:
            #获取下标题信息
            li_title = item.h4.string
            li_url = "https://www.dianping.com%s" % item.find_all("a")[0]["href"]
            if li_title == match_keyword:
                return li_url
        return ""


    def get_search_html(self):
        """
        页面抓取获取html内容
        :return:
        """
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Referer": "https://www.dianping.com/",
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
        }
        self.html = HttpOp.get_html_data(self.url, headers=headers)
