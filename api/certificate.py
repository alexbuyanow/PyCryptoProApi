"""
    PyCryptoPro API

    Certificates API
"""

from base64 import standard_b64decode
from flask_injector import inject
from flask_restful import abort, marshal_with
from connexion import request
from pycryptopro import CryptoProService, CertFilter
from .fields import CERT_FIELDS, CERT_LIST_FIELDS


def __get_certificate(cert_id, service: CryptoProService):
    """
    Gets certificate and checks if it exists
    """
    certificate = service.get_certificate(cert_id)
    if not certificate:
        abort(404)

    return certificate


@inject
@marshal_with(CERT_LIST_FIELDS)
def get_list(service: CryptoProService, search: str, limit: int, offset: int):
    """
    Gets certificates list
    """
    count, items = service.get_certificate_list(
        CertFilter(search, limit, offset)
    )
    return {'total': count, 'items': items}, 200


@inject
@marshal_with(CERT_FIELDS)
def get(service: CryptoProService, cert_id: str):
    """
    Gets certificate
    """
    return __get_certificate(cert_id, service)


@inject
def add(service: CryptoProService):
    """
    Adds certificate
    """
    file = standard_b64decode(request.json['file'])
    service.add_certificate(file)

    return {}, 201


@inject
def delete(service: CryptoProService, cert_id: str):
    """
    Removes certificate
    """
    __get_certificate(cert_id, service)
    service.remove_certificate(cert_id)

    return {}, 204
