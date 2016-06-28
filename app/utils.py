#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import *
import random
import string

def hash_generator(table):
    id_hash = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(3))
    p = table.select().where(table.id_hash == id_hash).dicts()
    while p:
        id_hash = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(3))
    return id_hash
