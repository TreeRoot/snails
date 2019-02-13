# -*- coding:utf-8 -*-


# date: 2019.02.13
# author: xwt



import sys
reload(sys)
sys.setdefaultencoding("utf-8")


from handlers.index import IndexHanfler


url = [
        (r"/", IndexHanfler)
        ]
