# src/data_loader/models.py

from pydantic import BaseModel, validator
from datetime import datetime
from typing import Literal

class Ticket(BaseModel):
    ticket_id: int
    category: Literal["network_issue", "billing_issue", "equipment_issue"]
    description: str
    timestamp: datetime

    @validator("description")
    def desctiption_not_empty(cls,v):
        if not v.strip():
            raise ValueError("Description cannot be empty")
        return v

