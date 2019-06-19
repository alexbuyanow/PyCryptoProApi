"""
    PyCryptoPro API

    Signatures API
"""

from base64 import standard_b64encode, standard_b64decode
from flask_injector import inject
from flask_restful import abort
from connexion import request
from pycryptopro import CryptoProService


@inject
def sign(service: CryptoProService):
    """
    Signs file
    """
    file = standard_b64decode(request.json['file'])
    sign_type = request.json['sign_type']
    sign_content = ''

    if sign_type == 'attached':
        sign_content = service.sign_attached(file, True, True)
    elif sign_type == 'detached':
        sign_content = service.sign_detached(file, True, True)
    else:
        abort(400)

    return {'sign': standard_b64encode(sign_content).decode('utf-8')}, 200


@inject
def validate(service: CryptoProService):
    """
    Validates file sign
    """
    file = standard_b64decode(request.json['file'])
    sign_type = request.json['sign_type']
    is_valid = False

    if sign_type == 'attached':
        is_valid = service.verify_attached(file, True, True)
    elif sign_type == 'detached':
        sign_content = standard_b64decode(request.json['sign'])
        is_valid = service.verify_detached(file, sign_content, True, True)
    else:
        abort(400)

    return {'valid': is_valid}, 200
