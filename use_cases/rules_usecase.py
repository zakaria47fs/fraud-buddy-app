import logging
from datetime import datetime

from objects.rules_dto import RulesObject
from services.mongo_service import MongoService


logger_use_case_info = logging.getLogger('rule_use_case_info')
logger_use_case_exception = logging.getLogger('rule_use_case_exception')
logger_use_case_exception.setLevel(logging.ERROR)
logger_use_case_info.setLevel(logging.INFO)


class RulesUseCase:

    def __init__(self):
        self.mongo_service = MongoService()
        self.collection_name = 'rules'

    def add_rule(self, rules_obj: RulesObject) -> dict:
        logger_use_case_info.info('%UC ********** start add rule **********%')
        rules_data = rules_obj.dict() # we can use jsonable_encoder instead
        rules_data.update({'created_at': datetime.now()})
        self.mongo_service.add_item_db(self.collection_name, rules_data)
        logger_use_case_info.info('%UC ********** end add rule **********%')
        return {"status": "success", "response": "rule is added successfully"}

    def get_rule(self, rule_id: int) -> dict:
        logger_use_case_info.info('%UC ********** start get rule **********%')
        data = self.mongo_service.get_item_db(self.collection_name, {'rule_id': rule_id})
        logger_use_case_info.info('%UC ********** end get rule **********%')
        return data

    def remove_rule(self, rule_id: int) -> dict:
        logger_use_case_info.info('%UC ********** start remove rule **********%')
        self.mongo_service.remove_item_db(self.collection_name, {'rule_id': rule_id})
        result = dict(response={"status": "success", "response": "rule is removed successfully"},
                        code=200)
        logger_use_case_info.info('%UC ********** end remove rule **********%')
        return result

    def update_rule(self, rule_id: int, rules_obj: RulesObject) -> dict:
        logger_use_case_info.info('%UC ********** start update rule **********%')
        self.mongo_service.update_item_db(self.collection_name, {'rule_id': rule_id}, rules_obj.to_dict())
        result = dict(response={"status": "success", "response": "rule is updated successfully"},
                        code=200)
        logger_use_case_info.info('%UC ********** end update rule **********%')
        return result

    def get_all_rules(self) -> list:
        logger_use_case_info.info('%UC ********** start get all rules **********%')
        data = self.mongo_service.get_all_items_db(self.collection_name)
        logger_use_case_info.info('%UC ********** end get all rules **********%')
        return list(data)

    def get_rules_by_filter(self, filters={}) -> list:
        logger_use_case_info.info('%UC ********** start get all rules **********%')
        data = self.mongo_service.filter_items_db(self.collection_name, filter=filters)
        logger_use_case_info.info('%UC ********** end get all rules **********%')
        return list(data)
