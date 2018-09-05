# -*- coding: utf-8 -*-

# @File    : spider.py
# @Date    : 2018-09-05
# @Author  : Peng Shiyu

from datetime import datetime
from pprint import pprint

import requests
from scrapy import Selector

from models import ProxyModel, IntegrityError
from proxy_source import *
from utils import get_md5


def get_html(url):
    print("request url: %s" % url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding
    return response.text


def parse(html, xpaths):
    tree = Selector(text=html)
    trs = tree.xpath(xpaths["trs"])

    for tr in trs:
        ip = xpath_extract(tr, xpaths.get("ip"))
        port = xpath_extract(tr, xpaths.get("port"))
        address = xpath_extract(tr, xpaths.get("address"))
        style = xpath_extract(tr, xpaths.get("style"), "透明")
        protocol = xpath_extract(tr, xpaths.get("protocol"), "HTTP")

        item = {
            "ip": ip,
            "port": port,
            "style": style_mapping.get(style, style),
            "protocol": protocol,
            "address": address,
            "source": xpaths.get("source", ""),
            "create_time": datetime.now(),
            "update_time": datetime.now(),
            "md5": get_md5("{}{}".format(ip, port))
        }

        pprint(item)
        yield item


def xpath_extract(selector, xpath_exp, default=""):
    try:
        text = selector.xpath(xpath_exp).extract_first("").strip()
    except TypeError:
        text = default

    return text


def save(item):
    if item["ip"] != "":
        try:
            ProxyModel.create(**item)
            print("### Success save %s" % item["ip"])
        except IntegrityError as e:
            print("### Error: %s" % e)


def crawl(index):
    proxy_item = proxy_list[index]
    html = get_html(proxy_item["url"])
    for item in parse(html, proxy_item):
        save(item)


def crawl_all():
    for index in range(len(proxy_list)):
        crawl(index)


if __name__ == '__main__':
    # crawl(proxy_list[3])
    crawl_all()
