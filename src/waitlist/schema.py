from ninja import Schema
from datetime import datetime
from pydantic import EmailStr
from typing import List, Any


class WaitlistEntryCreateSchema(Schema):
    email: EmailStr

class ErrorWaitlistEntryCreateSchema(Schema):
    email: List[Any]

class WaitlistEntryDetailSchema(Schema):
    email: EmailStr
    updated: datetime
    timestamp: datetime

class WaitlistEntryListSchema(Schema):
    id: int
    email: EmailStr