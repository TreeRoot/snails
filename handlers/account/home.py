# -*- coding:utf-8 -*-


from tornado.web import RequestHandler, authenticated


class home(RequestHandler):
    @authenticated
    def get(self):
        self.template()

