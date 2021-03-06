#!/usr/bin/env python
# -*- coding: utf-8 -*-

from peewee import *
import datetime

db = SqliteDatabase('db.db')


class User(Model):
    id = PrimaryKeyField()
    gid = CharField()
    name = CharField()
    nick = CharField()
    avatar = CharField()
    registered = DateField(default=datetime.date.today())

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.name)

    class Meta:
        database = db


class Plan(Model):
    id = PrimaryKeyField()
    nick = ForeignKeyField(User, to_field='nick')
    name = CharField()
    start = DateField()
    final = DateField()

    class Meta:
        database = db
