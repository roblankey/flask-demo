from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields


class ClientSchema(Schema):
    class Meta:
        type_ = 'client'
        self_view = 'client_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'client_list'

    id = fields.Integer(as_string=True, dump_only=True)
    name = fields.Str(required=True, load_only=True)
    display_name = fields.Function(lambda obj: "{}".format(obj.name.upper()))
    users = Relationship(self_view='client_users',
                         self_view_kwargs={'id': '<id>'},
                         related_view='user_list',
                         related_view_kwargs={'id': '<id>'},
                         many=True,
                         schema='UserSchema',
                         type_='user')


class UserSchema(Schema):
    class Meta:
        type_ = 'user'
        self_view = 'user_detail'
        self_view_kwargs = {'id': '<id>'}

    id = fields.Integer(as_string=True, dump_only=True)
    first_name = fields.Str(required=True, load_only=True)
    last_name = fields.Str(load_only=True)
    email = fields.Email(load_only=True)
    display_name = fields.Function(lambda obj: "{} {} <{}>".format(obj.first_name, obj.last_name, obj.email))
    client = Relationship(attribute='client',
                          self_view='user_client',
                          self_view_kwargs={'id': '<id>'},
                          related_view='client_detail',
                          related_view_kwargs={'user_id': '<id>'},
                          schema='ClientSchema',
                          type_='client')
