#!/bin/python2.7
# coding=utf-8
"""
提供基本http操作类
"""
import requests
import cookielib
import sys

class HttpOp(object):
    @staticmethod
    def get_html_data(url, headers={}):
        """
        获取下html内容
        """
        r = requests.get(url, headers=headers)
        html = r.text.encode(r.encoding).decode("utf-8")
        return html

    @staticmethod
    def get_html_cookie(url):
        """
        获取cookie信息
        :param url:
        :return:
        """
        #请求下url，获取下cookies
        r = requests.get(url)
        cookie_dict = requests.utils.dict_from_cookiejar(r.cookies)
        print cookie_dict
        sys.exit()