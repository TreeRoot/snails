# -*- conding:utf-8 -*-


from url import url


import tornado.web
import os


from settings.base import TEMPLATES, STATICS

settings = dict(
            template_path = TEMPLATES,
            static_path = STATICS,
        )

application = tornado.web.Application(
            handlers = url, 
            **settings
        )
