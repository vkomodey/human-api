import connexion
import six
import json
from typing import List
from hmt_escrow.validation_request import ValidationRequest
from human_api.models.bool_data_response import BoolDataResponse  # noqa: E501
from human_api.models.error_unauthorized_response import ErrorUnauthorizedResponse  # noqa: E501


def finish_validation_and_pay_rewards(
        request_addr: str,
        winning_validators: List[str],
        amounts: List[int],
        gas_payer: str,
        gas_payer_priv: str
    ):
    credentials = {
        "gas_payer": gas_payer,
        "gas_payer_priv": gas_payer_priv
    }
    validation_request = ValidationRequest(credentials, request_addr)

    try:
        result = validation_request.finish_validation_and_pay_rewards(winning_validators, amounts)

        return BoolDataResponse(result), 200
    except Exception as e:
        return ErrorUnauthorizedResponse(str(e)), 401
