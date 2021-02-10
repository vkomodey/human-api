# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from human_api.models.base_model_ import Model
from human_api import util


class JobListResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, jobs: List[str]=None):  # noqa: E501
        """JobListResponse - a model defined in Swagger

        :param jobs: The jobs of this JobListResponse.  # noqa: E501
        :type jobs: List[str]
        """
        self.swagger_types = {
            'jobs': List[str]
        }

        self.attribute_map = {
            'jobs': 'jobs'
        }
        self._jobs = jobs

    @classmethod
    def from_dict(cls, dikt) -> 'JobListResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The job_list_response of this JobListResponse.  # noqa: E501
        :rtype: JobListResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def jobs(self) -> List[str]:
        """Gets the jobs of this JobListResponse.


        :return: The jobs of this JobListResponse.
        :rtype: List[str]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs: List[str]):
        """Sets the jobs of this JobListResponse.


        :param jobs: The jobs of this JobListResponse.
        :type jobs: List[str]
        """

        self._jobs = jobs