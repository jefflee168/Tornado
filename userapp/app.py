import tornado.web
from handlers import user as user_handlers

HANDLERS = [
    (r"/api/users", user_handlers.UserListHandler)
]

def run():
    app = tornado.web.Application(
        HANDLERS,
        debug=True,
    )
    http_server = tornado.httpserver.HTTPServer(app)
    port = 8888
    print('server start on port: {}'.format(port))
    tornado.ioloop.IOLoop.instance().start()

if __name__ == 'main':
    run()
