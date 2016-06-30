#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import abort, request, jsonify
from flask_login import current_user
from flask_cors import cross_origin
from models import Plan
from utils import hash_id, unhash_id
from . import app

@app.route('/plans/<nick>', methods=['GET', 'POST', 'DELETE'])
@cross_origin()
def plans(nick):
    if request.method == 'GET':
        result = {'data':[]}
        p = Plan.select().where(Plan.nick == nick).dicts()
        for row in p:
            row['id'] = hash_id(row['id'])
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

@app.route('/plan/<pid>', methods=['GET', 'DELETE'])
@cross_origin()
def plan(pid):
    if request.method == 'GET':
        result = {'data':[]}
        pid = unhash_id(pid)
        p = Plan.select().where(Plan.id == pid)
        for row in p:
            row['id'] = hash_id(row['id'])
            result['data'].append(row)
        return jsonify(result)
    elif request.method == 'DELETE':
        payload = request.get_json(force = True)
        pid = unhash_id(payload['id'])
        p = Plan.delete().where(Plan.id = pid).execute()
        return jsonify(payload)