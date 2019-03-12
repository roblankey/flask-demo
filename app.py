# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_rest_jsonapi import Api, ResourceDetail, ResourceList, ResourceRelationship
# from flask_rest_jsonapi.exceptions import ObjectNotFound
# from sqlalchemy.orm.exc import NoResultFound
# from marshmallow_jsonapi.flask import Schema, Relationship
# from marshmallow_jsonapi import fields

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Client, User


# # Create logical data abstraction (same as data storage for this first example)
# class ClientSchema(Schema):
#     class Meta:
#         type_ = 'client'
#         self_view = 'client_detail'
#         self_view_kwargs = {'id': '<id>'}
#         self_view_many = 'client_list'
#
#     id = fields.Integer(as_string=True, dump_only=True)
#     name = fields.Str(required=True, load_only=True)
#     display_name = fields.Function(lambda obj: "{}".format(obj.name.upper()))
#     users = Relationship(self_view='client_users',
#                          self_view_kwargs={'id': '<id>'},
#                          related_view='user_list',
#                          related_view_kwargs={'id': '<id>'},
#                          many=True,
#                          schema='UserSchema',
#                          type_='user')
#
#
# class UserSchema(Schema):
#     class Meta:
#         type_ = 'user'
#         self_view = 'user_detail'
#         self_view_kwargs = {'id': '<id>'}
#
#     id = fields.Integer(as_string=True, dump_only=True)
#     first_name = fields.Str(required=True, load_only=True)
#     last_name = fields.Str(load_only=True)
#     email = fields.Email(load_only=True)
#     display_name = fields.Function(lambda obj: "{} {} <{}>".format(obj.first_name, obj.last_name, obj.email))
#     client = Relationship(attribute='client',
#                           self_view='user_client',
#                           self_view_kwargs={'id': '<id>'},
#                           related_view='client_detail',
#                           related_view_kwargs={'user_id': '<id>'},
#                           schema='ClientSchema',
#                           type_='client')
#
#
# # Create resource managers
# class ClientList(ResourceList):
#     schema = ClientSchema
#     data_layer = {'session': db.session,
#                   'model': Client}
#
#
# class ClientDetail(ResourceDetail):
#     def before_get_object(self, view_kwargs):
#         if view_kwargs.get('user_id') is not None:
#             try:
#                 user = self.session.query(User).filter_by(id=view_kwargs['user_id']).one()
#             except NoResultFound:
#                 raise ObjectNotFound({'parameter': 'user_id'}, "User: {} not found".format(view_kwargs['user_id']))
#             else:
#                 if user.client is not None:
#                     view_kwargs['id'] = user.client.id
#                 else:
#                     view_kwargs['id'] = None
#
#     schema = ClientSchema
#     data_layer = {'session': db.session,
#                   'model': Client,
#                   'methods': {'before_get_object': before_get_object}}
#
#
# class ClientRelationship(ResourceRelationship):
#     schema = ClientSchema
#     data_layer = {'session': db.session,
#                   'model': Client}
#
#
# class UserList(ResourceList):
#     def query(self, view_kwargs):
#         query_ = self.session.query(User)
#         if view_kwargs.get('id') is not None:
#             try:
#                 self.session.query(Client).filter_by(id=view_kwargs['id']).one()
#             except NoResultFound:
#                 raise ObjectNotFound({'parameter': 'id'}, "Client: {} not found".format(view_kwargs['id']))
#             else:
#                 query_ = query_.join(Client).filter(Client.id == view_kwargs['id'])
#         return query_
#
#     def before_create_object(self, data, view_kwargs):
#         if view_kwargs.get('id') is not None:
#             client = self.session.query(Client).filter_by(id=view_kwargs['id']).one()
#             data['client_id'] = client.id
#
#     schema = UserSchema
#     data_layer = {'session': db.session,
#                   'model': User,
#                   'methods': {'query': query,
#                               'before_create_object': before_create_object}}
#
#
# class UserDetail(ResourceDetail):
#     schema = UserSchema
#     data_layer = {'session': db.session,
#                   'model': User}
#
#
# class UserRelationship(ResourceRelationship):
#     schema = UserSchema
#     data_layer = {'session': db.session,
#                   'model': User}
    
    
# Create endpoints
# api = Api(app)
# api.route(ClientList, 'client_list', '/clients')
# api.route(ClientDetail, 'client_detail', '/clients/<int:id>', '/users/<int:user_id>/owner')
# api.route(ClientRelationship, 'client_users', '/clients/<int:id>/relationships/users')
# api.route(UserList, 'user_list', '/users', '/clients/<int:id>/users')
# api.route(UserDetail, 'user_detail', '/users/<int:id>')
# api.route(UserRelationship, 'user_client', '/users/<int:id>/relationships/owner')


@app.route('/')
def hello():
    return "Hello World!"


if __name__ == '__main__':
    # Start application
    app.run(debug=True)
