#!/bin/python2.7
# coding=utf-8
"""
提供基本http操作类
"""
import urllib2, urllib, sys


class HttpOp(object):
    @staticmethod
    def get_html_data(url, headers={}):
        """
        获取下html内容
        """
        print url
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        html = response.read()
        return html
