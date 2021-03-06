# coding: utf-8

"""
    demo

    validere  # noqa: E501

    The version of the OpenAPI document: 2.198.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class Tank(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'name': 'str',
        'site_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'site_id': 'site_id'
    }

    def __init__(self, id=None, name=None, site_id=None, local_vars_configuration=None):  # noqa: E501
        """Tank - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._site_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.site_id = site_id

    @property
    def id(self):
        """Gets the id of this Tank.  # noqa: E501

        Tank ID  # noqa: E501

        :return: The id of this Tank.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Tank.

        Tank ID  # noqa: E501

        :param id: The id of this Tank.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Tank.  # noqa: E501

        Tank Name  # noqa: E501

        :return: The name of this Tank.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Tank.

        Tank Name  # noqa: E501

        :param name: The name of this Tank.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def site_id(self):
        """Gets the site_id of this Tank.  # noqa: E501

        Site ID  # noqa: E501

        :return: The site_id of this Tank.  # noqa: E501
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this Tank.

        Site ID  # noqa: E501

        :param site_id: The site_id of this Tank.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and site_id is None:  # noqa: E501
            raise ValueError("Invalid value for `site_id`, must not be `None`")  # noqa: E501

        self._site_id = site_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Tank):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Tank):
            return True

        return self.to_dict() != other.to_dict()
