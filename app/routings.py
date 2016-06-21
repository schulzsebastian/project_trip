#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from . import app

@app.route('/')
def index():
    if current_user.is_authenticated():
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')