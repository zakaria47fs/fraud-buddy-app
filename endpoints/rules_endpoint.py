from fastapi import APIRouter
import logging

from objects.rules_dto import RulesObject
from use_cases.rules_usecase import CardValidateUseCase


rules_router = APIRouter()

logger_endpoint_info = logging.getLogger('rules_endpoint_info')
logger_endpoint_exception = logging.getLogger('rules_endpoint_exception')
logger_endpoint_exception.setLevel(logging.ERROR)
logger_endpoint_info.setLevel(logging.INFO)


@rules_router.post('/rules/add')
def add_rule(rules: RulesObject):
    logger_endpoint_info.info('********** start adding a rule **********')
    result_ = rules_usecase.add_rule(data)
    result = result_["response"]
    code = result_["code"]
    logger_endpoint_info.info('********** end adding a rule **********')
    return result, code


@rules_router.route('/rules/find/<id_rule>', methods=['GET'])
@marshal_with(ruleSchema)
def find_rule_id(id_rule, rule_use_case: ruleUseCaseFactory):
    logger_endpoint_info.info('********** start finding a rule **********')
    result = rule_use_case.get_find_rule(id_rule)
    logger_endpoint_info.info('********** end finding a rule **********')
    return result, 200


@rules_router.route('/rules/remove/<id_rule>', methods=['DELETE'])
def delete_rule_id(id_rule, rule_use_case: ruleUseCaseFactory):
    logger_endpoint_info.info('********** start removing a rule **********')
    try:
        result_ = rule_use_case.get_remove_rule(id_rule)
    except BadRequest:
        result_ = dict(response={"status": "failed", "response": str(sys.exc_info()[1])},
                       code=500)
    result = result_["response"]
    code = result_["code"]
    logger_endpoint_info.info('********** end removing a rule **********')
    return result, code


@rule_app.route('/rules/remove_many', methods=['DELETE'])
def delete_many_rules_id(rule_use_case: ruleUseCaseFactory):
    logger_endpoint_info.info('********** start removing a rule **********')
    try:
        data = request.get_json(force=True)
        result_ = rule_use_case.get_remove_many_rules(data["rules_id"])
    except BadRequest:
        result_ = dict(response={"status": "failed", "response": str(sys.exc_info()[1])},
                       code=500)
    result = result_["response"]
    code = result_["code"]
    logger_endpoint_info.info('********** end removing a rule **********')
    return result, code


@inject
@rule_app.route('/rules/update/<id_rule>', methods=['PUT'])
@jwt_required
def change_rule(id_rule, rule_use_case: ruleUseCaseFactory, rule_schema: ruleSchema):
    logger_endpoint_info.info('********** start changing a rule **********')
    try:
        data = request.get_json(force=True)
        validate_with(rule_schema, data)
        result_ = rule_use_case.get_update_rule(id_rule, data)
    except (BadRequest, InvalidSchemaError):
        result_ = dict(response={"status": "failed", "response": str(sys.exc_info()[1])},
                       code=500)
    result = result_["response"]
    code = result_["code"]
    logger_endpoint_info.info('********** end changing a rule **********')
    return result, code


@inject
@rule_app.route('/rules/update_many', methods=['PUT'])
@jwt_required
def change_many_rule(rule_use_case: ruleUseCaseFactory, rule_schema: UpdateManyruleSchema):
    logger_endpoint_info.info('********** start changing a rule **********')
    try:
        data = request.get_json(force=True)
        rule_data = remove_empty_values(data["payload"])
        validate_with(rule_schema, rule_data)
        if "date" in rule_data:
            rule_data["date"] = parser.parse(rule_data["date"])
        result_ = rule_use_case.get_update_many_rule(data["selected_records"], rule_data)
    except (BadRequest, InvalidSchemaError):
        result_ = dict(response={"status": "failed", "response": str(sys.exc_info()[1])},
                       code=500)
    result = result_["response"]
    code = result_["code"]
    logger_endpoint_info.info('********** end changing a rule **********')
    return result, code


@inject
@rule_app.route('/rules/findall', methods=['GET'])
@jwt_required
@marshal_with(FindruleSchema(many=True))
def find_all_rule(rule_use_case: ruleUseCaseFactory):
    logger_endpoint_info.info('********** start finding all rule **********')
    result = rule_use_case.get_find_all_rule()
    logger_endpoint_info.info('********** end finding all rule **********')
    return result, 200