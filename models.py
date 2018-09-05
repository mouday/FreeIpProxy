# -*- coding: utf-8 -*-

# @File    : models.py
# @Date    : 2018-09-05
# @Author  : Peng Shiyu

from peewee import *

db = SqliteDatabase("proxy.db")


class BaseModel(Model):
    class Meta:
        database = db


class ProxyModel(BaseModel):
    ip = CharField(null=True)
    port = CharField(null=True)
    style = CharField(default="透明")
    protocol = CharField(default="HTTP")
    address = CharField(default="")
    score = IntegerField(default=0)
    source = CharField(default="")
    md5 = CharField(unique=True)  # ip + port
    create_time = DateTimeField(default=None)
    update_time = DateTimeField(default=None)


if not ProxyModel.table_exists():
    ProxyModel.create_table()
