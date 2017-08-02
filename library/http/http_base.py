#!/bin/python2.7
# coding=utf-8
"""
提供基本http操作类
"""
import requests
import cookielib
import sys, os
import json
import base64

class HttpOp(object):
    @staticmethod
    def get_html_data(url, headers={}, cookies=None):
        """
        获取下html内容
        """
        r = requests.get(url, headers=headers, cookies=cookies)
        if r.status_code != 200 or (not r.text):
            return ""
        return r.text.encode(r.encoding).decode("utf-8")

    @staticmethod
    def get_html_cookie(url):
        """
        获取cookie信息
        :param url:
        :return:
        """
        cookie_file_encode = base64.encodestring(url)
        cookie_file = "cookies/%s.txt" % cookie_file_encode
        #判断下文件是否存在，从文件中读取
        if os.path.isfile(cookie_file):
            f = open(cookie_file, 'r')
            cookie_file_string = f.read()
            cookie_dict = json.loads(cookie_file_string)
            return requests.utils.cookiejar_from_dict(cookie_dict)
        #请求下url，获取下cookies
        r = requests.get(url)
        cookie_dict = requests.utils.dict_from_cookiejar(r.cookies)
        cookie_dict_string = json.dumps(cookie_dict)
        #写入cookie文件
        print cookie_file_encode
        f = open(cookie_file, 'w')
        f.write(cookie_dict_string)
        f.close()
        return r.cookies