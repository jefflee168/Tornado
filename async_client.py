import time

import tornado.gen
import tornado.httpclient
import tornado.ioloop
from tornado import gen

N = 10
URL = 'http://localhost:8888/sleep'

@gen.coroutine
def main():
	http_client = tornado.httpclient.AsyncHTTPClient()
	response = yield [
	    http_client.fetch(URL) for i in range(N)
	]

beg1 = time.time()
tornado.ioloop.IOLoop.current().run_sync(main)
print('async',time.time()-beg1)