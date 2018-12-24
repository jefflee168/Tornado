#-*- coding: utf-8 -*-

from tornado import gen
from tornado.httpclient import AsyncHTTPClient

@gen.coroutine
def coroutine_visit():
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch("www.baidu.com")
    print(response.body)