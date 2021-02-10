# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from human_api.models.base_model_ import Model
from human_api import util


class NetworkStatsResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, network_id: int=None, network_name: str=None, factory_count: int=None, job_count: int=None, total_payouts: int=None):  # noqa: E501
        """NetworkStatsResponse - a model defined in Swagger

        :param network_id: The network_id of this NetworkStatsResponse.  # noqa: E501
        :type network_id: int
        :param network_name: The network_name of this NetworkStatsResponse.  # noqa: E501
        :type network_name: str
        :param factory_count: The factory_count of this NetworkStatsResponse.  # noqa: E501
        :type factory_count: int
        :param job_count: The job_count of this NetworkStatsResponse.  # noqa: E501
        :type job_count: int
        :param total_payouts: The total_payouts of this NetworkStatsResponse.  # noqa: E501
        :type total_payouts: int
        """
        self.swagger_types = {
            'network_id': int,
            'network_name': str,
            'factory_count': int,
            'job_count': int,
            'total_payouts': int
        }

        self.attribute_map = {
            'network_id': 'networkId',
            'network_name': 'network_name',
            'factory_count': 'factory_count',
            'job_count': 'job_count',
            'total_payouts': 'total_payouts'
        }
        self._network_id = network_id
        self._network_name = network_name
        self._factory_count = factory_count
        self._job_count = job_count
        self._total_payouts = total_payouts

    @classmethod
    def from_dict(cls, dikt) -> 'NetworkStatsResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The network_stats_response of this NetworkStatsResponse.  # noqa: E501
        :rtype: NetworkStatsResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def network_id(self) -> int:
        """Gets the network_id of this NetworkStatsResponse.


        :return: The network_id of this NetworkStatsResponse.
        :rtype: int
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id: int):
        """Sets the network_id of this NetworkStatsResponse.


        :param network_id: The network_id of this NetworkStatsResponse.
        :type network_id: int
        """

        self._network_id = network_id

    @property
    def network_name(self) -> str:
        """Gets the network_name of this NetworkStatsResponse.


        :return: The network_name of this NetworkStatsResponse.
        :rtype: str
        """
        return self._network_name

    @network_name.setter
    def network_name(self, network_name: str):
        """Sets the network_name of this NetworkStatsResponse.


        :param network_name: The network_name of this NetworkStatsResponse.
        :type network_name: str
        """

        self._network_name = network_name

    @property
    def factory_count(self) -> int:
        """Gets the factory_count of this NetworkStatsResponse.


        :return: The factory_count of this NetworkStatsResponse.
        :rtype: int
        """
        return self._factory_count

    @factory_count.setter
    def factory_count(self, factory_count: int):
        """Sets the factory_count of this NetworkStatsResponse.


        :param factory_count: The factory_count of this NetworkStatsResponse.
        :type factory_count: int
        """

        self._factory_count = factory_count

    @property
    def job_count(self) -> int:
        """Gets the job_count of this NetworkStatsResponse.


        :return: The job_count of this NetworkStatsResponse.
        :rtype: int
        """
        return self._job_count

    @job_count.setter
    def job_count(self, job_count: int):
        """Sets the job_count of this NetworkStatsResponse.


        :param job_count: The job_count of this NetworkStatsResponse.
        :type job_count: int
        """

        self._job_count = job_count

    @property
    def total_payouts(self) -> int:
        """Gets the total_payouts of this NetworkStatsResponse.


        :return: The total_payouts of this NetworkStatsResponse.
        :rtype: int
        """
        return self._total_payouts

    @total_payouts.setter
    def total_payouts(self, total_payouts: int):
        """Sets the total_payouts of this NetworkStatsResponse.


        :param total_payouts: The total_payouts of this NetworkStatsResponse.
        :type total_payouts: int
        """

        self._total_payouts = total_payouts