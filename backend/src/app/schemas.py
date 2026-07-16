from pydantic import BaseModel
from typing import Optional

class SurveyCreate(BaseModel):
    respondent_name: Optional[str]
    location: Optional[str]
    score: int
    notes: Optional[str]

class SurveyOut(SurveyCreate):
    id: int
    created_at: Optional[str]

    class Config:
        orm_mode = True
