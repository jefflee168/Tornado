import tornado.web
from tornado.esape import json_encode
from models.user import UserModel

class UserListHandler(tornado.web.RequestHandler):
    def get(self):
        users = UserModel.get_all()
        self.write(json_encode(users))

    def post(self):
        name = self.get_argument('name')
        age = self.get_argument('age')
        UserModel.create(name, age)
        resp = {'status': True, 'msg': 'create success'}
        self.write(json_encode(resp))