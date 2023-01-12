from typing import List, Optional
from bson import ObjectId
from pydantic import BaseModel, Field
from datetime import datetime


class BinValidatorObject(BaseModel):
    issuing_countries_include: List[str]
    issuing_countries_exclude: List[str]
    issuing_brands_include: List[str]
    issuing_brands_exclude: List[str]
    instutions_include: List[str]
    instutions_exclude: List[str]


class RulesObject(BaseModel):
    rule_id: int
    name: str
    luhn_check_enable: bool
    bin_validator_enable: bool
    bin_validator_options: BinValidatorObject
    created_at: Optional[datetime]
