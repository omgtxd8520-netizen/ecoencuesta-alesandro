from .db import db

async def create_survey(s):
    query = "INSERT INTO surveys (respondent_name, location, score, notes) VALUES (:respondent_name, :location, :score, :notes) RETURNING id, created_at"
    values = s.dict()
    row = await db.fetch_one(query=query, values=values)
    return {**values, 'id': row['id'], 'created_at': row['created_at']}

async def get_survey(survey_id: int):
    query = "SELECT id, respondent_name, location, score, notes, created_at FROM surveys WHERE id = :id"
    return await db.fetch_one(query=query, values={'id': survey_id})
