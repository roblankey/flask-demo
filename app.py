# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_rest_jsonapi import Api

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from resources import *

api = Api(app)
api.route(ClientList, 'client_list', '/clients')
api.route(ClientDetail, 'client_detail', '/clients/<int:id>', '/users/<int:user_id>/owner')
api.route(ClientRelationship, 'client_users', '/clients/<int:id>/relationships/users')
api.route(UserList, 'user_list', '/users', '/clients/<int:id>/users')
api.route(UserDetail, 'user_detail', '/users/<int:id>')
api.route(UserRelationship, 'user_client', '/users/<int:id>/relationships/owner')


if __name__ == '__main__':
    app.run()
