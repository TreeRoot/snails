# -*- codnig:utf-8 -*-

import tornado.ioloop
import tornado.options 
import tornado.httpserver


from application import application
from tornado.options import define, options

define("port", default=8970, help="run on given port", type=int)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)

    print("Development server is running at http:127.0.0.1:%s" % options.port)

    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
