# -*- coding: utf-8 -*-

# @File    : utils.py
# @Date    : 2018-09-05
# @Author  : Peng Shiyu
import hashlib


def get_md5(key):
    return hashlib.md5(key.encode()).hexdigest()
