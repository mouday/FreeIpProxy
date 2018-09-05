# -*- coding: utf-8 -*-

# @File    : proxy_source.py
# @Date    : 2018-09-05
# @Author  : Peng Shiyu

# 代理抓取配置目录 ：https://www.jianshu.com/p/93fd64a2747b

"""
配置参数说明：
"source": 来源
"url": 网页地址
"trs": 选择列表xpath表达式，返回每一行组成的列表
"ip": 选择ip地址的xpath表达式
"port": 选择port端口的xpath表达式
"address": 选择address服务器地址的xpath表达式
"style": 选择style类型（透明 或高匿）的xpath表达式
"protocol": 选择protocol协议（HTTP 或HTTPS）的xpath表达式

备注： 如果没有指定xpath表达式，默认为空
特殊：style默认为"透明"，protocol默认"HTTP"
"""

proxy_list = [
    {
        "source": "西刺代理",
        "url": "http://www.xicidaili.com/nn/",
        "trs": "//*[@id='ip_list']//tr",
        "ip": "./td[2]/text()",
        "port": "./td[3]/text()",
        "address": "./td[4]/text()",
        "style": "./td[5]/text()",
        "protocol": "./td[6]/text()"
    },
    {
        "source": "89ip代理",
        "url": "http://www.89ip.cn/",
        "trs": "//table[@class='layui-table']//tr",
        "ip": "./td[1]/text()",
        "port": "./td[2]/text()",
        "address": "./td[3]/text()",
    },

    {
        "source": "云代理",
        "url": "http://www.ip3366.net/free/?stype=1",
        "trs": "//*[@id='list']//tr",
        "ip": "./td[1]/text()",
        "port": "./td[2]/text()",
        "style": "./td[3]/text()",
        "protocol": "./td[4]/text()",
        "address": "./td[5]/text()",
    },
    {
        "source": "快代理",
        "url": "https://www.kuaidaili.com/free/inha/",
        "trs": "//*[@id='list']//tr",
        "ip": "./td[1]/text()",
        "port": "./td[2]/text()",
        "style": "./td[3]/text()",
        "protocol": "./td[4]/text()",
        "address": "./td[5]/text()",
    },
]

# 是否高匿类型转换
style_mapping = {
    "高匿": "高匿",
    "高匿名": "高匿",
    "透明": "透明",
    "高匿代理IP": "高匿",
    "普通代理IP": "透明",
    "透明代理IP": "透明"
}
