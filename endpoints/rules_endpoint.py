from fastapi import APIRouter
import logging
from typing import List

from objects.rules_dto import RulesObject
from use_cases.rules_usecase import RulesUseCase


rules_router = APIRouter()

logger_endpoint_info = logging.getLogger('rules_endpoint_info')
logger_endpoint_exception = logging.getLogger('rules_endpoint_exception')
logger_endpoint_exception.setLevel(logging.ERROR)
logger_endpoint_info.setLevel(logging.INFO)


@rules_router.post('/rules/add', tags=['Rules'])
def add_rule(rules: RulesObject):
    logger_endpoint_info.info('********** start adding a rule **********')
    result = RulesUseCase().add_rule(rules)
    logger_endpoint_info.info('********** end adding a rule **********')
    return result, 200


@rules_router.get('/rules/find/<rule_id>', response_model=RulesObject, tags=['Rules'])
def find_rule_id(rule_id):
    logger_endpoint_info.info('********** start finding a rule **********')
    result = RulesUseCase().get_rule(rule_id)
    logger_endpoint_info.info('********** end finding a rule **********')
    return result


@rules_router.delete('/rules/remove/<rule_id>', tags=['Rules'])
def delete_rule_id(rule_id):
    logger_endpoint_info.info('********** start removing a rule **********')
    result = RulesUseCase().remove_rule(rule_id)
    logger_endpoint_info.info('********** end removing a rule **********')
    return result, 200


@rules_router.put('/rules/update/<rule_id>', tags=['Rules'])
def update_rule(rule_id, rules: RulesObject):
    logger_endpoint_info.info('********** start changing a rule **********')
    result = RulesUseCase().update_rule(rule_id, rules)
    logger_endpoint_info.info('********** end changing a rule **********')
    return result, 200


@rules_router.get('/rules/findall', response_model=List[RulesObject], tags=['Rules'])
def find_all_rules():
    logger_endpoint_info.info('********** start finding all rule **********')
    result = RulesUseCase().get_all_rules()
    print(result)
    logger_endpoint_info.info('********** end finding all rule **********')
    return result
