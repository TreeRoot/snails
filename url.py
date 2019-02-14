# -*- coding:utf-8 -*-


# date: 2019.02.13
# author: xwt


from handlers.account.login import login
from handlers.account.home import home 


url = [
        (r"/login", login),
        (r"/home", home),
    ]
