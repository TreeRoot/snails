# -*- conding:utf-8 -*-


import hashlib

from data.db import metadb
from handlers.requests.requests_wrap import requests_wrap


class user_login(requests_wrap):
    def get(self):
        self.template()

    def post(self):

        user_id = username = self.get_argument("username", None)
        password = self.get_argument("password", None)

        if not password or not username:
            msg = { "code" : 1, "status": 1, "msg": "no password or username", "data": []}
            self.json(msg)

        # set cookie
        token = self.new_token()
        self.on_login_success(token, user_id)

        msg = { "code" : 0, "status": 0, "msg": "login success", "data": []}
        self.json(msg)


class user_register(requests_wrap):
    def get(self):
        self.template()

    def post(self):
        username = self.get_argument("username", None)
        password = self.get_argument("password", None)
        passwordr = self.get_argument("passwordr", None)

        if password == passwordr and username and password:
            msg = {"code":0, "status":0, "msg":"register success", "data": []}
            self.json(msg)

        else:
            msg = {"code":1, "status":1, "msg":"register fail", "data": []}
            self.json(msg)
