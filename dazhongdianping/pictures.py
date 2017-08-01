#!/bin/python2.7
# coding=utf-8
"""
采集下点评的图片信息
"""
from library.http.http_base import HttpOp
from bs4 import BeautifulSoup
import sys
class Picture(object):
    # 详情页面的url
    detail_url = None
    # 图片信息列表
    picture_list = []

    def __init__(self, detail_url):
        self.detail_url = detail_url

    def get_picture(self):
        """
        获取下所有的图片信息
        :return:
        """
        for i in range(1, 10):
            print "开始抓取第%s页的图片信息" % i
            pic_page_url = "%s/photos?pg=%s" % (self.detail_url, i)
            pic_html = self.get_picture_html(pic_page_url)
            pic_html_soup = BeautifulSoup(pic_html, "lxml")
            pic_ul_ele = pic_html_soup.find("div", class_="picture-list").ul
            if pic_ul_ele.text.strip() == "":
                break
            #开始提取图片信息
            self.get_picture_detail(pic_ul_ele)
        return self.picture_list

    def get_picture_detail(self, pic_ul_ele):
        """
        获取图片具体的信息
        :param pic_ul_ele:
        :return:
        """
        pic_li_ele_list = pic_ul_ele.find_all("li", class_="J_list", recursive=False)
        for pic_li_item in pic_li_ele_list:
            pic_detail = {}
            # 获取span hook的下一个元素
            span_hook = pic_li_item.find("span", class_="hook")
            pic_li_a = span_hook.find_next("a")
            if not pic_li_a:
                continue
            # 提取图片地址
            pic_detail["thumb_pic"] = pic_li_a.img.attrs["src"]
            # 图片大图地址
            pic_detail["big_pic"] = self.get_picture_bigpic(pic_li_a.attrs["href"])
            # 提取下上传用户和上传时间
            pic_li_info = pic_li_item.find("div", class_="picture-info").find("div", class_="info")
            pic_detail["upuser"] = pic_li_info.a.text
            pic_detail["uptimestr"] = pic_li_info.span.text
            self.picture_list.append(pic_detail)


    def get_picture_bigpic(self, url):
        """
        获取图片大图地址
        :param url:
        :return:
        """
        url = "https://www.dianping.com%s" % url
        html = self.get_picture_html(url)
        soup = BeautifulSoup(html, "lxml")
        pic_ele = soup.select("#J_pic-wrap")
        pic_ele_image = pic_ele[0].find("img")
        return pic_ele_image.attrs["src"]

    def get_picture_html(self, url):
        """
        获取图片页面html
        :param url:
        :return:
        """
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
