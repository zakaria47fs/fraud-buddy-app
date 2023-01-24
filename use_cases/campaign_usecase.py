import logging

from objects.campaign_dto import CampaignObject
from services.mongo_service import MongoService

logger_use_case_info = logging.getLogger('campaign_use_case_info')
logger_use_case_exception = logging.getLogger('campaign_use_case_exception')
logger_use_case_exception.setLevel(logging.ERROR)
logger_use_case_info.setLevel(logging.INFO)


class CampaignUseCase:

    def __init__(self):
        self.mongo_service = MongoService()
        self.collection_name = 'campaigns'

    def add_campaign(self, campaign_obj: CampaignObject) -> dict:
        logger_use_case_info.info('%UC ********** start add campaign **********%')
        campaign_data = campaign_obj.dict()
        self.mongo_service.add_item_db(self.collection_name, campaign_data)
        result = dict(response={"status": "success", "response": "campaign is added successfully"},
                        code=200)
        logger_use_case_info.info('%UC ********** end add campaign **********%')
        return result

    def get_campaign(self, campaign_id: int) -> dict:
        logger_use_case_info.info('%UC ********** start get campaign **********%')
        result = self.mongo_service.get_item_db(self.collection_name, {'campaign_id': campaign_id})
        logger_use_case_info.info('%UC ********** end get campaign **********%')
        return result

    def remove_campaign(self, campaign_id: int) -> dict:
        logger_use_case_info.info('%UC ********** start remove campaign **********%')
        self.mongo_service.remove_item_db(self.collection_name, {'campaign_id': campaign_id})
        result = dict(response={"status": "success", "response": "campaign is removed successfully"},
                        code=200)
        logger_use_case_info.info('%UC ********** end remove campaign **********%')
        return result

    def update_campaign(self, campaign_id: int, campaign_obj: CampaignObject) -> dict:
        logger_use_case_info.info('%UC ********** start update campaign **********%')
        self.mongo_service.update_item_db(self.collection_name, {'campaign_id': campaign_id}, campaign_obj.to_dict())
        result = dict(response={"status": "success", "response": "campaign is updated successfully"},
                        code=200)
        logger_use_case_info.info('%UC ********** end update campaign **********%')
        return result

    def get_all_campaign(self) -> list:
        logger_use_case_info.info('%UC ********** start get all campaign **********%')
        result = self.mongo_service.get_all_items_db(self.collection_name)
        logger_use_case_info.info('%UC ********** end get all campaign **********%')
        return result