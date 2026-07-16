from .db import get_db
from bson import ObjectId
import datetime

async def create_survey(s):
    db = get_db()
    doc = s.dict()
    doc['created_at'] = datetime.datetime.utcnow()
    result = await db.surveys.insert_one(doc)
    doc['id'] = str(result.inserted_id)
    return doc

async def get_survey(survey_id: str):
    db = get_db()
    try:
        oid = ObjectId(survey_id)
    except Exception:
        return None
    doc = await db.surveys.find_one({'_id': oid})
    if not doc:
        return None
    doc['id'] = str(doc.pop('_id'))
    return doc
