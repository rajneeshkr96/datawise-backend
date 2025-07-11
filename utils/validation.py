from marshmallow import Schema, fields

class DatasetSchema(Schema):
    name = fields.String(required=True)
    owner = fields.String(required=True)
    description = fields.String()
    tags = fields.List(fields.String())

class QualityLogSchema(Schema):
    status = fields.String(required=True)
    details = fields.String(required=True)
