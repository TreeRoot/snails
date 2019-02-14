# -*- coding:utf-8 -*-


# date: 2019.02.13
# author: xwt


from handlers.account.user_common import user_login, user_register
from handlers.account.home import home


url = [
        (r"/register", user_register),
        (r"/login", user_login),
        (r"/home", home),
    ]
