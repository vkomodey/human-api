# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from human_api.models.base_model_ import Model
from human_api import util


class JobStatusResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, status: str = None):  # noqa: E501
        """JobStatusResponse - a model defined in Swagger

        :param status: The status of this JobStatusResponse.  # noqa: E501
        :type status: str
        """
        self.swagger_types = {'status': str}

        self.attribute_map = {'status': 'status'}
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'JobStatusResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The job_status_response of this JobStatusResponse.  # noqa: E501
        :rtype: JobStatusResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def status(self) -> str:
        """Gets the status of this JobStatusResponse.


        :return: The status of this JobStatusResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this JobStatusResponse.


        :param status: The status of this JobStatusResponse.
        :type status: str
        """
        allowed_values = ["Launched", "Pending", "Partial", "Paid", "Complete",
                          "Cancelled"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError("Invalid value for `status` ({0}), must be one of {1}".format(
                status, allowed_values))

        self._status = status
