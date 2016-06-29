#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import abort, request, jsonify
from flask_login import current_user
from flask_cors import cross_origin
from models import Plan
from . import app

@app.route('/plans/<nick>', methods=['GET', 'POST', 'DELETE'])
@cross_origin()
def plans(nick):
    if request.method == 'GET':
        result = {'data':[]}
        p = Plan.select().where(Plan.nick == nick).dicts()
        for row in p:
            result['data'].append(row)
        return jsonify(result)
    elif request.method == 'POST':
    	payload = request.get_json(force = True)
    	p = Plan.create(**payload)
        return jsonify(payload)
    elif request.method == 'DELETE':
        payload = request.get_json(force = True)
        p = Plan.delete().where((Plan.name == payload['name']) & (Plan.nick == payload['nick'])).execute()
        return jsonify(payload)