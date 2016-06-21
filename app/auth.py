#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import redirect, url_for, session, request, render_template
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_oauthlib.client import OAuth
from models import *
from . import app

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

oauth = OAuth()
google = oauth.remote_app(
    'google',
    consumer_key=app.config.get('GOOGLE_ID'),
    consumer_secret=app.config.get('GOOGLE_SECRET'),
    request_token_params={
        'scope': 'email'
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)

@login_manager.user_loader
def load_user(id):
    return User.select().where(User.id == id).first()

@app.route('/login')
def login():
    return google.authorize(callback=url_for('authorized', _external=True))


@app.route('/logout')
def logout():
    session.pop('google_token', None)
    logout_user()
    return redirect(url_for('index'))


@app.route('/authorized')
def authorized():
    resp = google.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )

    session['google_token'] = (resp['access_token'], '')
    me = google.get('userinfo')
    user = User.select().where(User.gid == me.data['id']).first()
    if not user:
        user = User.create(
            gid=me.data['id'],
            name=me.data['name'],
            email=me.data['email'],
            avatar=me.data['picture']
        )
    login_user(user)
    return redirect(url_for('index'))


@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')