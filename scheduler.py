# -*- coding: utf-8 -*-

# @File    : scheduler.py
# @Date    : 2018-09-05
# @Author  : Peng Shiyu

from apscheduler.schedulers.background import BackgroundScheduler

from check import check_all
from spider import crawl_all
from config import *


def start_scheduler():
    # 实例化一个调度器
    scheduler = BackgroundScheduler()

    # 添加任务并设置触发方式
    scheduler.add_job(crawl_all, 'interval', seconds=CRAWL_INTERVAL)
    scheduler.add_job(check_all, 'interval', seconds=CHECK_INTERVAL)

    # 开始运行调度器
    print("start scheduler...")
    scheduler.start()
