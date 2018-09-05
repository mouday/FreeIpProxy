# -*- coding: utf-8 -*-

# @File    : check.py
# @Date    : 2018-09-05
# @Author  : Peng Shiyu

from datetime import datetime

import requests

from config import *
from models import ProxyModel


def get_status(_proxy):
    """
    通过访问百度检测代理ip有效性
    @param _proxy:
    @return:
    """
    url = "https://www.baidu.com/"
    proxies = {
        "http": "http://{}".format(_proxy),
        "https": "https://{}".format(_proxy)
    }
    try:
        response = requests.get(url, proxies=proxies, timeout=5)
        status_code = response.status_code
    except Exception as e:
        status_code = e
    return status_code


def check_all():
    rows = ProxyModel.select().order_by(ProxyModel.update_time).limit(10)
    for row in rows:
        proxy = "{}:{}".format(row.ip, row.port)
        status = get_status(proxy)
        print(row.id, proxy, status, row.source)

        if status == 200:
            score = int(row.score) + 1
        else:
            score = int(row.score) - 1

        ProxyModel.update(
            update_time=datetime.now(), score=score
        ).where(ProxyModel.id == row.id).execute()

        if score < MIN_SCORE:
            ret = ProxyModel.delete().where(ProxyModel.id == row.id).execute()
            print("delete ret: %s" % ret)


if __name__ == '__main__':
    check_all()
