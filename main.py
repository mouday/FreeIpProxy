# -*- coding: utf-8 -*-

# @File    : main.py
# @Date    : 2018-09-05
# @Author  : Peng Shiyu


import json
from datetime import datetime

from flask import Flask

from check import check_all
from models import ProxyModel
from spider import crawl_all, crawl
from scheduler import start_scheduler

app = Flask(__name__)


@app.route("/")
def index():
    return "hello"


@app.route("/get")
def get_proxy():
    row = ProxyModel.select().order_by(-ProxyModel.score).first()
    item = dict()
    for k, v in row.__data__.items():
        if isinstance(v, datetime):
            v = v.strftime("%Y-%m-%d %H:%M:%S")
        item[k] = v

    return json.dumps(item)


@app.route("/get_list/<int:count>")
def get_proxy_list(count):
    rows = ProxyModel.select().order_by(-ProxyModel.score).limit(count)

    lst = []
    for row in rows:
        item = dict()

        for k, v in row.__data__.items():
            if isinstance(v, datetime):
                v = v.strftime("%Y-%m-%d %H:%M:%S")
            item[k] = v
        lst.append(item)

    return json.dumps(lst)


@app.route("/crawl")
def crawl_proxy_all():
    crawl_all()
    return "ok"


@app.route("/crawl/<int:index>")
def crawl_proxy(index):
    crawl(index)
    return "ok"


@app.route("/delete/<uid>")
def delete_proxy(uid):
    ret = ProxyModel.delete().where(ProxyModel.id == uid).execute()
    return "ret: %s" % ret


@app.route("/check")
def check_proxy():
    check_all()
    return "check ok"


if __name__ == '__main__':
    start_scheduler()
    app.run()
