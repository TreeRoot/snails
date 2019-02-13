# -*- conding:utf-8 -*-


import hashlib

from data.db import metadb
from handlers.requests.requests_wrap import requests_wrap


class MainHandler(requests_wrap):
    def get(self):
        self.render("login.html")

    def post(self):
        username = self.get_argument("username", None)
        password = self.get_argument("password", None)

        if not password or not username:
            msg = {
                    "code" : 1,
                    "status": 1,
                    "msg": "no password or username",
                    "data": []
                }

            self.json(msg)

    def get_origin(self):
        pass



