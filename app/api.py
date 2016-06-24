#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import abort, request, jsonify
from flask_login import current_user
from . import app
from models import *

@app.route('/plans/<nick>', methods=['GET'])
def plans(nick):
    if request.method == 'GET':
        result = {'data':[]}
        rs = Plan.select().where(Plan.nick==nick).dicts()
        for row in rs:
            result['data'].append(row)
        return jsonify(result)