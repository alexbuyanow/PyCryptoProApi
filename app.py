"""
    PyCryptoPro API

    Application
"""

import connexion
from flask import Response, json
from injector import Binder
from flask_injector import FlaskInjector
from pycryptopro import (
    CryptoProService,
    CryptoProviderFactory,
    Config,
    CryptoProException
)


def crypto_pro_error(exception: CryptoProException) -> Response:
    """
    Handles CryptoPro exceptions
    """
    return Response(
        response=json.dumps({
            'code': exception.code,
            'message': exception.message,
        }),
        status=400,
        mimetype="application/json"
    )


def get_config() -> Config:
    """
    Gets config
    """
    return Config({
        'cert_manager_path': '/opt/cprocsp/bin/amd64/certmgr',
        'cryptocp_path': '/opt/cprocsp/bin/amd64/cryptcp',
        'temp_path': '/tmp',
        'storage_name': 'ca',
        'sign_storage_name': 'uMy',
        'sign_storage_pin': '123'
    })


def configure(binder: Binder) -> Binder:
    """
    Sets DI configurations
    """
    config = get_config()
    provider_factory = CryptoProviderFactory(config)
    binder.bind(
        CryptoProService,
        to=CryptoProService(provider_factory, config),
    )

    return binder


def create_app():
    """
    Creates application
    """
    app = connexion.App(__name__)
    app.add_api('api.yaml')
    app.add_error_handler(CryptoProException, crypto_pro_error)

    FlaskInjector(app=app.app, modules=[configure])

    return app


if __name__ == '__main__':
    create_app().run(port=5000)
