#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello,Tornado")

def make_app():
    return tornado.web.Application([
	(r"/",MainHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.lister(8888)
    tornado.ioloop.IOLoop.current().start()
