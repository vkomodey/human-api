# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from human_api.models.base_model_ import Model
from human_api.models.network_list_response_networks import NetworkListResponseNetworks  # noqa: F401,E501
from human_api import util


class NetworkListResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, networks: List[NetworkListResponseNetworks]=None):  # noqa: E501
        """NetworkListResponse - a model defined in Swagger

        :param networks: The networks of this NetworkListResponse.  # noqa: E501
        :type networks: List[NetworkListResponseNetworks]
        """
        self.swagger_types = {
            'networks': List[NetworkListResponseNetworks]
        }

        self.attribute_map = {
            'networks': 'networks'
        }
        self._networks = networks

    @classmethod
    def from_dict(cls, dikt) -> 'NetworkListResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The network_list_response of this NetworkListResponse.  # noqa: E501
        :rtype: NetworkListResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def networks(self) -> List[NetworkListResponseNetworks]:
        """Gets the networks of this NetworkListResponse.


        :return: The networks of this NetworkListResponse.
        :rtype: List[NetworkListResponseNetworks]
        """
        return self._networks

    @networks.setter
    def networks(self, networks: List[NetworkListResponseNetworks]):
        """Sets the networks of this NetworkListResponse.


        :param networks: The networks of this NetworkListResponse.
        :type networks: List[NetworkListResponseNetworks]
        """

        self._networks = networks