from flask_rest_jsonapi import ResourceDetail, ResourceList, ResourceRelationship
from flask_rest_jsonapi.exceptions import ObjectNotFound
from sqlalchemy.orm.exc import NoResultFound

from app import db
from models import Client, User
from schema import ClientSchema, UserSchema


class ClientList(ResourceList):
    schema = ClientSchema
    data_layer = {'session': db.session,
                  'model': Client}


class ClientDetail(ResourceDetail):
    def before_get_object(self, view_kwargs):
        if view_kwargs.get('user_id') is not None:
            try:
                user = self.session.query(User).filter_by(id=view_kwargs['user_id']).one()
            except NoResultFound:
                raise ObjectNotFound({'parameter': 'user_id'}, "User: {} not found".format(view_kwargs['user_id']))
            else:
                if user.client is not None:
                    view_kwargs['id'] = user.client.id
                else:
                    view_kwargs['id'] = None

    schema = ClientSchema
    data_layer = {'session': db.session,
                  'model': Client,
                  'methods': {'before_get_object': before_get_object}}


class ClientRelationship(ResourceRelationship):
    schema = ClientSchema
    data_layer = {'session': db.session,
                  'model': Client}


class UserList(ResourceList):
    def query(self, view_kwargs):
        query_ = self.session.query(User)
        if view_kwargs.get('id') is not None:
            try:
                self.session.query(Client).filter_by(id=view_kwargs['id']).one()
            except NoResultFound:
                raise ObjectNotFound({'parameter': 'id'}, "Client: {} not found".format(view_kwargs['id']))
            else:
                query_ = query_.join(Client).filter(Client.id == view_kwargs['id'])
        return query_

    def before_create_object(self, data, view_kwargs):
        if view_kwargs.get('id') is not None:
            client = self.session.query(Client).filter_by(id=view_kwargs['id']).one()
            data['client_id'] = client.id

    schema = UserSchema
    data_layer = {'session': db.session,
                  'model': User,
                  'methods': {'query': query,
                              'before_create_object': before_create_object}}


class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {'session': db.session,
                  'model': User}


class UserRelationship(ResourceRelationship):
    schema = UserSchema
    data_layer = {'session': db.session,
                  'model': User}
