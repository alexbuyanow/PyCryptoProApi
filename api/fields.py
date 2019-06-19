"""
    PyCryptoPro API

    Marshaled fields
"""

from flask_restful import fields


INFO_FIELDS = {
    'inn': fields.String,
    'ogrn': fields.String,
    'street': fields.String,
    'email': fields.String,
    'country': fields.String,
}

CERT_FIELDS = {
    'id': fields.String(attribute='identifier'),
    'subject': fields.Nested(INFO_FIELDS),
    'issuer': fields.Nested(INFO_FIELDS),
    'valid_from': fields.DateTime,
    'valid_to': fields.DateTime,
    'serial': fields.String,
    'thumbprint': fields.String
}

CERT_LIST_FIELDS = {
    'total': fields.Integer,
    'items': fields.Nested(CERT_FIELDS)
}

CRL_FIELDS = {
    'id': fields.String(attribute='identifier'),
    'issuer': fields.Nested(INFO_FIELDS),
    'update': fields.DateTime,
    'next_update': fields.DateTime
}

CRL_LIST_FIELDS = {
    'total': fields.Integer,
    'items': fields.Nested(CRL_FIELDS)
}
