#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for, abort
from flask_login import login_required, current_user
from . import app

@app.route('/')
def index():
    if current_user.is_authenticated():
        return redirect(url_for('dashboard', nick=current_user.nick))
    return render_template('index.html')

@app.route('/dashboard/<nick>')
@login_required
def dashboard(nick):
    if current_user.nick != nick:
        abort(404)
    return render_template('dashboard.html')