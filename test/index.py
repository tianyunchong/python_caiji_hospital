#!/bin/python2.7
# coding=utf-8
"""
计算两个字符串的相似度
"""
import difflib

def get_like_score(a, b):
    """
    获取两个字符串相似度
    :param a:
    :param b:
    :return:
    """
    seq = difflib.SequenceMatcher(None, a, b)
    return seq.ratio()


a = "郑州大桥医院"
b = "大桥医院"
c = "大桥医院停车场"
d = "小飞象母婴用品(大桥医院店)"
e = "私人订制"
print get_like_score(a, e)
