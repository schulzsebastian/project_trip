#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hashids import Hashids
from . import app


def hash_id(id_unhashed):
    hashid_instance = Hashids(salt=app.config['SECRET_KEY'])
    return hashid_instance.encode(id_unhashed)


def unhash_id(id_hashed):
    try:
        hashid_instance = Hashids(salt=app.config['SECRET_KEY'])
        return hashid_instance.decode(hash_id)[0]
    except:
        return False
