# coding: utf-8

# flake8: noqa

"""
    demo

    validere  # noqa: E501

    The version of the OpenAPI document: 2.198.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from openapi_client.api.default_api import DefaultApi

# import ApiClient
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
from openapi_client.exceptions import OpenApiException
from openapi_client.exceptions import ApiTypeError
from openapi_client.exceptions import ApiValueError
from openapi_client.exceptions import ApiKeyError
from openapi_client.exceptions import ApiException
# import models into sdk package
from openapi_client.models.bad_request import BadRequest
from openapi_client.models.not_found import NotFound
from openapi_client.models.tank import Tank
from openapi_client.models.tank_request import TankRequest
from openapi_client.models.unauthorized import Unauthorized

