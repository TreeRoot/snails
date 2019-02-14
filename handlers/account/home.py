# -*- coding:utf-8 -*-


import tornado
from handlers.requests.requests_wrap import requests_wrap


class home(requests_wrap):
    @tornado.web.authenticated
    def get(self):
        self.template()

