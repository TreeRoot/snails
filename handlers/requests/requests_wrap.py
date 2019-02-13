# -*- coding:utf-8 -*-


import json
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


        

