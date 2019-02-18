# -*- conding:utf-8 -*-


import hashlib

from db_manage.db import metadb
from handlers.requests.requests_wrap import requests_wrap
from handlers.utils.common import point_dict


class user_login(requests_wrap):
    def get(self):
        if self.current_user:
            self.redirect('/home')
            return
        self.template()

    def post(self):

        username = self.get_argument("username", None)
        password = self.get_argument("password", None)

        if not password or not username:
            self.msg(code=1, msg='password or username does not exist')
            return

        user = metadb.user.find_one({"username": username})
        if user.get('password') == password:
            # set cookie
            self.on_login_success(self.new_token(), user['_id'])

            # self.redirect('/home')
            self.msg(msg='login success')

        else:
            self.msg(code=1, msg='password or username error')
            return


class user_register(requests_wrap):
    def get(self):
        self.template()

    def post(self):
        obj = self.get_args('username', 'password', 'password_confirm', 'code_btn', 'phone_num')

        if obj.password == obj.password_confirm and obj.username and obj.password:
            if self.check_repet(obj.username):
                _id = metadb.user.save(obj)
                self.msg(msg='success')

            else:
                self.msg(code=1, msg='username alerady used')

        else:
            self.msg(code=1, msg="register failed")

    def check_repet(self, name):
        all_names = [username['username'] for username in list(metadb.user.find({}, {'username':1, '_id':0}))]
        if name in all_names:
            return False
        else:
            return True
