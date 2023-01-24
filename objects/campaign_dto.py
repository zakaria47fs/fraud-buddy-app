from typing import List, Optional
from bson import ObjectId
from pydantic import BaseModel, Field
from datetime import datetime


class CampaignObject(BaseModel):
    campaign_id: int
    name: str
    rule_id: int
