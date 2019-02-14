# -*- conding:utf-8 -*-


from url import url


import tornado.web
import os


from settings.base import TEMPLATES, STATICS

settings = dict(
            debug = True,
            template_path = TEMPLATES,
            static_path = STATICS,
            cookie_secret = 'ddddddddddddd',
            login_url = '/login'
        )

application = tornado.web.Application(
            handlers = url, 
            **settings
        )
