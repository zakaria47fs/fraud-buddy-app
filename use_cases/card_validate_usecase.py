import logging

from services.mongo_service import MongoService
from utils.utils import luhn_check
from objects.rules_dto import RulesObject
from objects.requests_dto import CardValidateResponseObject


logger_use_case_info = logging.getLogger('profile_use_case_info')
logger_use_case_exception = logging.getLogger('profile_use_case_exception')
logger_use_case_exception.setLevel(logging.ERROR)
logger_use_case_info.setLevel(logging.INFO)


class CardValidateUseCase:

    def __init__(self):
        self.mongo_service = MongoService()
        self.rules_collection = 'rules'
        self.campaigns_collection = 'campaigns'

    def validate_card_number(self, campaign_id: int, card_number: int) -> dict:
        logger_use_case_info.info('%UC ********** start validate_card_number **********%')
        response = CardValidateResponseObject(valid=True)
        campaign = self.mongo_service.get_item_db(self.campaigns_collection, campaign_id)
        rules = self.mongo_service.get_item_db(self.rules_collection, campaign.get('rule_id'))
        if not rules:
            return {'response': f"error, rule_id {campaign.get('rule_id')} specified not found", 'code': 500}
        rules_data = RulesObject(**rules)
        #validation process
        if rules_data.luhn_check_enable and luhn_check(card_number)==False:
            response.valid = False
            return response
        if rules_data.bin_validator_enable:
            pass

        logger_use_case_info.info('%UC ********** end validate_card_number **********%')
        return response
