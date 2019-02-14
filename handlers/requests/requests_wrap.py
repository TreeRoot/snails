# -*- coding:utf-8 -*-


import os
import json
import inspect
import binascii

from tornado.web import RequestHandler


class requests_wrap(RequestHandler):

    __token__ = {}

    def new_token(self):
        while True:
            new_token = binascii.hexlify(os.urandom(16)).decode("utf8")
            if new_token not in self.__token__:
                return new_token

    def on_login_success(self, new_token, user_id):
        self.set_secure_cookie("_token", new_token)
        self.__token__.update({new_token:user_id})

    def get_current_user(self):
        """
            get token from cookie
        """

        token = self.get_secure_cookie("_token")
        if token and token.decode() in self.__token__:
            user_id = self.__token__[token.decode()]
            return user_id

        return None

    def check_auth(self):
        token = self.get_secure_cookie("_token")
        if token:
            return token.decode() in self.__token__

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
