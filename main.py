# -*- coding: utf-8 -*-

# @File    : main.py
# @Date    : 2018-09-05
# @Author  : Peng Shiyu


import json
from datetime import datetime

from flask import Flask, jsonify

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

    return jsonify(item)


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

    return jsonify(lst)


@app.route("/crawl")
def crawl_proxy_all():
    crawl_all()
    return jsonify({
            "status": 0,
            "msg": "ok"
        })


@app.route("/crawl/<int:index>")
def crawl_proxy(index):
    crawl(index)
    return jsonify({
        "status": 0,
        "msg": "ok"
    })


@app.route("/delete/<uid>")
def delete_proxy(uid):
    ret = ProxyModel.delete().where(ProxyModel.id == uid).execute()
    return jsonify({
        "status": 0,
        "msg": "ok",
        "rows": ret
    })


@app.route("/check")
def check_proxy():
    check_all()
    return jsonify({
        "status": 0,
        "msg": "ok",
    })


if __name__ == '__main__':
    start_scheduler()
    app.run(host="0.0.0.0", port=8002, debug=True)
