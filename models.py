from webapi.core import db


class User(db.Model):
    username = db.VarcharField(max_length=30)
    password = db.HashField(type='md5')
    email = db.EmailField()


class Role(db.Model):
    name = db.VarcharField()
    users = db.ForeignKeyField(User, 'roles')