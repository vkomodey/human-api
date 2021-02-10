# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from human_api.models.base_model_ import Model
from human_api import util


class FactoryCreateBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, gas_payer: str=None, gas_payer_private: str=None, network_id: int=0):  # noqa: E501
        """FactoryCreateBody - a model defined in Swagger

        :param gas_payer: The gas_payer of this FactoryCreateBody.  # noqa: E501
        :type gas_payer: str
        :param gas_payer_private: The gas_payer_private of this FactoryCreateBody.  # noqa: E501
        :type gas_payer_private: str
        :param network_id: The network_id of this FactoryCreateBody.  # noqa: E501
        :type network_id: int
        """
        self.swagger_types = {
            'gas_payer': str,
            'gas_payer_private': str,
            'network_id': int
        }

        self.attribute_map = {
            'gas_payer': 'gasPayer',
            'gas_payer_private': 'gasPayerPrivate',
            'network_id': 'networkId'
        }
        self._gas_payer = gas_payer
        self._gas_payer_private = gas_payer_private
        self._network_id = network_id

    @classmethod
    def from_dict(cls, dikt) -> 'FactoryCreateBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The factory_create_body of this FactoryCreateBody.  # noqa: E501
        :rtype: FactoryCreateBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def gas_payer(self) -> str:
        """Gets the gas_payer of this FactoryCreateBody.


        :return: The gas_payer of this FactoryCreateBody.
        :rtype: str
        """
        return self._gas_payer

    @gas_payer.setter
    def gas_payer(self, gas_payer: str):
        """Sets the gas_payer of this FactoryCreateBody.


        :param gas_payer: The gas_payer of this FactoryCreateBody.
        :type gas_payer: str
        """

        self._gas_payer = gas_payer

    @property
    def gas_payer_private(self) -> str:
        """Gets the gas_payer_private of this FactoryCreateBody.


        :return: The gas_payer_private of this FactoryCreateBody.
        :rtype: str
        """
        return self._gas_payer_private

    @gas_payer_private.setter
    def gas_payer_private(self, gas_payer_private: str):
        """Sets the gas_payer_private of this FactoryCreateBody.


        :param gas_payer_private: The gas_payer_private of this FactoryCreateBody.
        :type gas_payer_private: str
        """

        self._gas_payer_private = gas_payer_private

    @property
    def network_id(self) -> int:
        """Gets the network_id of this FactoryCreateBody.


        :return: The network_id of this FactoryCreateBody.
        :rtype: int
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id: int):
        """Sets the network_id of this FactoryCreateBody.


        :param network_id: The network_id of this FactoryCreateBody.
        :type network_id: int
        """

        self._network_id = network_id