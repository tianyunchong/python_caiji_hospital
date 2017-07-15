#!/bin/python2.7
# coding=utf-8
"""
提供基本http操作类
"""
import urllib2


class HttpOp(object):
    @staticmethod
    def get_html_data(url):
        """
        获取下html内容
        """
        response = urllib2.urlopen(url)
        html = response.read()
        return html
