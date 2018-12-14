#/usr/bin/env python
# -*- coding: utf-8 -*-

import os,time
import datetime as dt

import tornado.gen
import tornado.httpserver
import tornado.ioloop
import tornado.web

class SleepHandler(tornado.web.RequestHandler):
    def get(self):
        time.sleep(5)
	self.write(str(dt.datetime.now()))

if __name__ == "__main__":
    app = tornado.web.Application(
	[
	    (r"/sleep", SleepHandler)
	]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
