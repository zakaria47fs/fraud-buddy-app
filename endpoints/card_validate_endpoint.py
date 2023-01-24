from fastapi import APIRouter
import logging

from objects.requests_dto import CardValidateRequestObject, CardValidateResponseObject
from use_cases.card_validate_usecase import CardValidateUseCase


card_validate_router = APIRouter()

logger_endpoint_info = logging.getLogger('card_validator_endpoint_info')
logger_endpoint_exception = logging.getLogger('card_validator_endpoint_exception')
logger_endpoint_exception.setLevel(logging.ERROR)
logger_endpoint_info.setLevel(logging.INFO)


@card_validate_router.post('/card_validate', response_model=CardValidateResponseObject, tags=['CardValidate'])
def card_validate(request: CardValidateRequestObject):
    logger_endpoint_info.info('********** start card_validate_router **********')
    result = CardValidateUseCase().validate_card_number(request.campaign_id, request.card_number)
    logger_endpoint_info.info('********** end card_validate_router **********')
    return result

