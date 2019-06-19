"""
    PyCryptoPro API

    CRLs API
"""

from base64 import standard_b64decode
from flask_injector import inject
from flask_restful import abort, marshal_with
from pycryptopro import CryptoProService, CertFilter
from connexion import request
from .fields import CRL_FIELDS, CRL_LIST_FIELDS


def __get_crl(cert_id, service: CryptoProService):
    """
    Gets crl and checks if it exists
    """
    crl = service.get_crl(cert_id)
    if not crl:
        abort(404)

    return crl


@inject
@marshal_with(CRL_LIST_FIELDS)
def get_list(service: CryptoProService, search: str, limit: int, offset: int):
    """
    Gets CRLs list
    """
    count, items = service.get_crl_list(
        CertFilter(search, limit, offset)
    )
    return {'total': count, 'items': items}, 200


@inject
@marshal_with(CRL_FIELDS)
def get(service: CryptoProService, cert_id: str):
    """
    Gets CRL
    """
    return __get_crl(cert_id, service)


@inject
def add(service: CryptoProService):
    """
    Adds CRL
    """
    file = standard_b64decode(request.json['file'])
    service.add_crl(file)

    return {}, 201


@inject
def delete(service: CryptoProService, cert_id: str):
    """
    Removes CRL
    """
    __get_crl(cert_id, service)
    service.remove_crl(cert_id)

    return {}, 204
