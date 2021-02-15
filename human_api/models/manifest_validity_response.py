# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from human_api.models.base_model_ import Model
from human_api.models.error_parameter_response import ErrorParameterResponse  # noqa: F401,E501
from human_api import util


class ManifestValidityResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self,
                 valid: bool = None,
                 errors: List[ErrorParameterResponse] = None):  # noqa: E501
        """ManifestValidityResponse - a model defined in Swagger

        :param valid: The valid of this ManifestValidityResponse.  # noqa: E501
        :type valid: bool
        :param errors: The errors of this ManifestValidityResponse.  # noqa: E501
        :type errors: List[ErrorParameterResponse]
        """
        self.swagger_types = {'valid': bool, 'errors': List[ErrorParameterResponse]}

        self.attribute_map = {'valid': 'valid', 'errors': 'errors'}
        self._valid = valid
        self._errors = errors

    @classmethod
    def from_dict(cls, dikt) -> 'ManifestValidityResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The manifest_validity_response of this ManifestValidityResponse.  # noqa: E501
        :rtype: ManifestValidityResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def valid(self) -> bool:
        """Gets the valid of this ManifestValidityResponse.


        :return: The valid of this ManifestValidityResponse.
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid: bool):
        """Sets the valid of this ManifestValidityResponse.


        :param valid: The valid of this ManifestValidityResponse.
        :type valid: bool
        """

        self._valid = valid

    @property
    def errors(self) -> List[ErrorParameterResponse]:
        """Gets the errors of this ManifestValidityResponse.


        :return: The errors of this ManifestValidityResponse.
        :rtype: List[ErrorParameterResponse]
        """
        return self._errors

    @errors.setter
    def errors(self, errors: List[ErrorParameterResponse]):
        """Sets the errors of this ManifestValidityResponse.


        :param errors: The errors of this ManifestValidityResponse.
        :type errors: List[ErrorParameterResponse]
        """

        self._errors = errors
