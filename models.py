#!/usr/bin/env python
# -*- coding: utf-8 -*-

from peewee import *

db = SqliteDatabase('db.db')

class User(Model):
    gid = CharField()
    name = CharField(unique=True)
    email = CharField()
    avatar = CharField()

    class Meta:
        database = db