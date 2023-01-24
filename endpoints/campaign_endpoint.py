from fastapi import APIRouter
import logging

from objects.campaign_dto import CampaignObject
from use_cases.campaign_usecase import CampaignUseCase


campaign_router = APIRouter()

logger_endpoint_info = logging.getLogger('campaign_endpoint_info')
logger_endpoint_exception = logging.getLogger('campaign_endpoint_exception')
logger_endpoint_exception.setLevel(logging.ERROR)
logger_endpoint_info.setLevel(logging.INFO)


@campaign_router.post('/campaign/add', tags=['Campaign'])
def add_campaign(campaign: CampaignObject):
    logger_endpoint_info.info('********** start adding a campaign **********')
    result_ = CampaignUseCase().add_campaign(campaign)
    result = result_["response"]
    code = result_["code"]
    logger_endpoint_info.info('********** end adding a campaign **********')
    return result, 200


@campaign_router.get('/campaign/find/<campaign_id>', tags=['Campaign'])
def find_campaign_id(campaign_id):
    logger_endpoint_info.info('********** start finding a campaign **********')
    result = CampaignUseCase().get_campaign(campaign_id)
    logger_endpoint_info.info('********** end finding a campaign **********')
    return result, 200


@campaign_router.delete('/campaign/remove/<campaign_id>', tags=['Campaign'])
def delete_campaign_id(campaign_id):
    logger_endpoint_info.info('********** start removing a campaign **********')
    result_ = CampaignUseCase().remove_campaign(campaign_id)
    result = result_["response"]
    code = result_["code"]
    logger_endpoint_info.info('********** end removing a campaign **********')
    return result, code


@campaign_router.put('/campaign/update/<campaign_id>', tags=['Campaign'])
def update_campaign(campaign_id, campaign: CampaignObject):
    logger_endpoint_info.info('********** start changing a campaign **********')
    result_ = CampaignUseCase().update_campaign(campaign_id, campaign)
    result = result_["response"]
    code = result_["code"]
    logger_endpoint_info.info('********** end changing a campaign **********')
    return result, code


@campaign_router.get('/campaign/findall', tags=['Campaign'])
def find_all_campaign():
    logger_endpoint_info.info('********** start finding all campaign **********')
    result = CampaignUseCase().get_all_campaign()
    logger_endpoint_info.info('********** end finding all campaign **********')
    return result, 200
