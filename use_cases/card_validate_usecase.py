import logging
from bson.objectid import ObjectId

from objects import ProfileSchema, ProfileData, ProfileFilterSchema
from services.mongo_service import MongoService
from utils.utils import luhn_check

logger_use_case_info = logging.getLogger('profile_use_case_info')
logger_use_case_exception = logging.getLogger('profile_use_case_exception')
logger_use_case_exception.setLevel(logging.ERROR)
logger_use_case_info.setLevel(logging.INFO)


class CardValidateUseCase:

    def __init__(self):
        self.mongo_service = MongoService()

    def validate_card_number(self, campaign_id: int, card_number: int) -> dict:
        logger_use_case_info.info('%UC ********** start add profile **********%')
        rules = self.mongo_service.get_item_db()
        self.mongo_service.add_profile_db(profile_data.data())
        result = dict(response={"status": "success", "response": "profile is added successfully"},
                        code=200)
        logger_use_case_info.info('%UC ********** end add profile **********%')
        return result