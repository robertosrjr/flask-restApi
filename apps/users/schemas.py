# -*- coding: utf-8 -*-

from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()
    email = fields.Email()
    cpf = fields.Str()