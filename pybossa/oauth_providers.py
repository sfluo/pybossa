# -*- coding: utf8 -*-
# This file is part of PYBOSSA.
#
# Copyright (C) 2016 Scifabric LTD.
#
# PYBOSSA is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PYBOSSA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PYBOSSA.  If not, see <http://www.gnu.org/licenses/>.
from flask_oauthlib.client import OAuth

OAuthProviders = ['twitter', 'facebook', 'google', 'wechat', 'weibo']

class Weibo(object):
 
    """Class Weibo to enable Wechat signin."""
 
    def __init__(self, app=None):
        """Init method."""
        self.app = app
        if app is not None:  # pragma: no cover
            self.init_app(app)
 
    def init_app(self, app):
        """Init app using factories."""
        self.oauth = OAuth().remote_app(
             'weibo',
             base_url='https://api.weibo.com/2/',
             request_token_url=None, #'https://a.com.cn/oauth/request_token',
             access_token_method="POST",
             access_token_url='https://api.weibo.com/oauth2/access_token', 
             authorize_url='https://api.weibo.com/oauth2/authorize',
             consumer_key=app.config['WEIBO_APP_ID'],
             consumer_secret=app.config['WEIBO_APP_SECRET'],
             content_type="application/json"
        )

class Wechat(object):
 
    """Class Wechat to enable Wechat signin."""
 
    def __init__(self, app=None):
        """Init method."""
        self.app = app
        if app is not None:  # pragma: no cover
            self.init_app(app)
 
    def init_app(self, app):
        """Init app using factories."""
        self.oauth = OAuth().remote_app(
             'wechat',
             base_url='https://api.weixin.qq.com/sns/',
             request_token_url=None,
             access_token_url='https://api.weixin.qq.com/sns/oauth2/access_token',
             authorize_url='https://open.weixin.qq.com/connect/oauth2/authorize',
             consumer_key=app.config['WECHAT_APP_ID'],
             consumer_secret=app.config['WECHAT_APP_SECRET'])

class Wechat(object):

    """Class Wechat to enable Wechat signin."""

    def __init__(self, app=None):
        """Init method."""
        self.app = app
        if app is not None:  # pragma: no cover
            self.init_app(app)

    def init_app(self, app):
        """Init app using factories."""
        self.oauth = OAuth().remote_app(
            'wechat',
            base_url='https://api.weixin.qq.com/sns/',
            request_token_url=None,
            access_token_url='https://api.weixin.qq.com/sns/oauth2/access_token',
            authorize_url='https://open.weixin.qq.com/connect/oauth2/authorize',
            consumer_key=app.config['WECHAT_APP_ID'],
            consumer_secret=app.config['WECHAT_APP_SECRET'])

class Twitter(object):

    """Class Twitter to enable Twitter signin."""

    def __init__(self, app=None):
        """Init method."""
        self.app = app
        if app is not None:  # pragma: no cover
            self.init_app(app)

    def init_app(self, app):
        """Init app using factories."""
        self.oauth = OAuth().remote_app(
            'twitter',
            base_url='https://api.twitter.com/1/',
            request_token_url='https://api.twitter.com/oauth/request_token',
            access_token_url='https://api.twitter.com/oauth/access_token',
            authorize_url='https://api.twitter.com/oauth/authenticate',
            consumer_key=app.config['TWITTER_CONSUMER_KEY'],
            consumer_secret=app.config['TWITTER_CONSUMER_SECRET'])


class Facebook(object):

    """Class Facebook to enable Facebook signin."""

    def __init__(self, app=None):
        """Init method."""
        self.app = app
        if app is not None:  # pragma: no cover
            self.init_app(app)

    def init_app(self, app):
        """Init app using factories pattern."""
        self.oauth = OAuth().remote_app(
            'facebook',
            base_url='https://graph.facebook.com/',
            request_token_url=None,
            access_token_url='/oauth/access_token',
            authorize_url='https://www.facebook.com/dialog/oauth',
            consumer_key=app.config['FACEBOOK_APP_ID'],
            consumer_secret=app.config['FACEBOOK_APP_SECRET'],
            request_token_params={'scope': 'email'})


class Google(object):

    """Class Google to enable Google signin."""

    def __init__(self, app=None):
        """Init method."""
        self.app = app
        if app is not None:  # pragma: no cover
            self.init_app(app)

    def init_app(self, app):
        """Init app using factories pattern."""
        self.oauth = OAuth().remote_app(
            'google',
            base_url='https://www.googleapis.com/oauth2/v1/',
            authorize_url='https://accounts.google.com/o/oauth2/auth',
            request_token_url=None,
            request_token_params={'scope': 'profile email'},
            access_token_url='https://accounts.google.com/o/oauth2/token',
            access_token_method='POST',
            consumer_key=app.config['GOOGLE_CLIENT_ID'],
            consumer_secret=app.config['GOOGLE_CLIENT_SECRET'])

class Flickr(object):

    def __init__(self, app=None):
        self.app = app
        if app is not None:  # pragma: no cover
            self.init_app(app)

    def init_app(self, app):  # pragma: no cover
        from flask import session
        self.app = app
        self.oauth = OAuth().remote_app(
            'flickr',
            request_token_url='https://www.flickr.com/services/oauth/request_token',
            access_token_url='https://www.flickr.com/services/oauth/access_token',
            authorize_url='https://www.flickr.com/services/oauth/authorize',
            consumer_key=app.config['FLICKR_API_KEY'],
            consumer_secret=app.config['FLICKR_SHARED_SECRET'],
            access_token_method='GET')
