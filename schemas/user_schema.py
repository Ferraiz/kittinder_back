from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str(required=True, validate=must_not_be_blank)
    password = fields.Str(required=True, validate=must_not_be_blank)
