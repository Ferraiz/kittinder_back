from marshmallow import Schema, fields

from schemas.validators import must_not_be_blank


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Email(
        required=True)
    password = fields.Str(
        required=True)
