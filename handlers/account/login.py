# -*- conding:utf-8 -*-


import hashlib

from data.db import metadb
from handlers.requests.requests_wrap import requests_wrap


class login(requests_wrap):
    def get(self):
        if self.check_auth():
            self.redirect('/home')
        else:
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

    def check_auth(self):
        token = self.get_secure_cookie("_token")
        if token:
            return token.decode() in self.__token__

    



