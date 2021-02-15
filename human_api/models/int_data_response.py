# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from human_api.models.base_model_ import Model
from human_api import util


class IntDataResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, data: int = None):  # noqa: E501
        """IntDataResponse - a model defined in Swagger

        :param data: The data of this IntDataResponse.  # noqa: E501
        :type data: int
        """
        self.swagger_types = {'data': int}

        self.attribute_map = {'data': 'data'}
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'IntDataResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The int_data_response of this IntDataResponse.  # noqa: E501
        :rtype: IntDataResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self) -> int:
        """Gets the data of this IntDataResponse.


        :return: The data of this IntDataResponse.
        :rtype: int
        """
        return self._data

    @data.setter
    def data(self, data: int):
        """Sets the data of this IntDataResponse.


        :param data: The data of this IntDataResponse.
        :type data: int
        """

        self._data = data
