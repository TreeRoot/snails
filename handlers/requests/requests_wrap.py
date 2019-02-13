# -*- coding:utf-8 -*-


import json
import os
import inspect

from tornado.web import RequestHandler


class requests_wrap(RequestHandler):

    def json(self, 
            obj, 
            content_type="text/javascript; charset=utf-8",
            cls=None
            ):
        """
            序列化
        """
        self.set_header("Content-Type", content_type)
        self.write(json.dumps(obj, cls=cls).replace("</", "<\\/"))

    def template(self, name=None, **kwargs):
        """
            优先以name命名的模板，函数名次之
            templates/account/login.html 对应handler/account/login.py
        """

        path = self.get_template_dir() + '/' + self.get_template_name() + '.html'

        self.render(path, **kwargs)

    def get_template_name(self):
        name = self.__class__.__name__.split('.')[0]
        return name

    def get_template_dir(self):
        root = os.path.dirname(inspect.getfile(self.__class__)).split('/')[-1]
        return root





        

