from marshmallow import Schema, fields

from schemas.validators import must_not_be_blank


class FavsSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(
        required=True, validate=must_not_be_blank)
    image = fields.Str()
