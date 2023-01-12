from typing import List, Optional
from bson import ObjectId
from pydantic import BaseModel, Field
from datetime import datetime


class CardValidateRequestObject(BaseModel):
    campaign_id: int
    card_number: int
