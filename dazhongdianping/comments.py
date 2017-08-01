#!/bin/python2.7
# coding=utf-8
from library.http.http_base import HttpOp
import os, sys
from bs4 import BeautifulSoup
import re

"""
获取评论信息
"""


class Comments(object):
    # 详情页面url
    detail_url = None
    # 评论结果列表
    comment_list = []

    def __init__(self, detail_url):
        self.detail_url = detail_url

    def get_comments(self):
        """
        获取下评论信息列表
        :return:
        """
        for i in range(1, 20):
            comment_url = "%s/review_all?pageno=%s" % (self.detail_url.rstrip("/"), i)
            print comment_url
            comment_html = self.get_comments_html(comment_url)
            beautySoup = BeautifulSoup(comment_html, "lxml")
            soup_comment_list = beautySoup.find("div", class_="comment-list")
            if soup_comment_list == None:
                break
            soup_comment_ul = soup_comment_list.findChild("ul")
            if soup_comment_ul.text.strip() == "":
                break
            # 开始获取评论的具体内容
            self.get_comment_detail(soup_comment_ul)
        return self.comment_list

    def get_comment_detail(self, ul_element):
        soup_comment_li = ul_element.find_all("li", recursive=False)
        for li_key, li_item in enumerate(soup_comment_li):
            print "开始收集第%s个评论" % li_key
            comment_item_dict = {}
            #提取下评论的用户头像和用户名
            li_item_pic = li_item.find("div", class_="pic")
            li_item_userinfo = li_item_pic.findChild("img")
            comment_item_dict["avatar"] = li_item_userinfo.attrs["src"]
            comment_item_dict["username"] = li_item_userinfo.attrs["title"]
            #提取下评论星级
            comment_item_dict["level"] = self.get_comments_detail_level(li_item)
            # 提取下评论的详情信息
            li_item_detail = li_item.find("div", class_="J_brief-cont")
            detail = ""
            for item_detail in li_item_detail.contents:
                detail += str(item_detail).encode("utf-8")
            comment_item_dict["detail"] = detail
            self.comment_list.append(comment_item_dict)

    def get_comments_detail_level(self, li_item):
        """
        获取下评论的星级信息
        :param li_item:
        :return:
        """
        li_item_rst = li_item.find("div", class_="user-info").findChildren()
        if not li_item_rst:
            return 0
        li_item_rst_level = li_item_rst[0].attrs["class"]
        li_item_rst_level_class = li_item_rst_level[1] if len(li_item_rst_level) > 1 else ""
        li_item_rst_level_class_match = re.findall(r"irr-star(\d+)", li_item_rst_level_class)
        if len(li_item_rst_level_class_match) > 0:
            return li_item_rst_level_class_match[0]
        else:
            return 0

    def get_comments_html(self, url):
        "获取评论信息页面"
        cookies = HttpOp.get_html_cookie("https://www.dianping.com/")
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Connection": "keep-alive",
            "Host": "www.dianping.com",
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
        }
        return HttpOp.get_html_data(url, headers=headers, cookies=cookies)
