from app import db


class Client(db.Model):
    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def __str__(self):
        return '{}'.format(self.name)


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    client = db.relationship('Client', backref=db.backref('users'))

    def __init__(self, first_name, last_name, email, client):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.client_id = client.id
        self.client = client

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def __str__(self):
        return '{} {} <{}>'.format(self.first_name, self.last_name, self.email)
