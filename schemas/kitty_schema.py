from flask import Response
from marshmallow import Schema, fields

from schemas.validators import must_not_be_blank
# from schemas.user_schema import UserSchema


class KittySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(
        required=True, validate=must_not_be_blank)
    photo = fields.Str(required=True, validate=must_not_be_blank)
    # user_id = fields.Nested(UserSchema)
