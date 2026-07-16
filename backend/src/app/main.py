from fastapi import FastAPI, HTTPException
from . import db, crud, schemas

app = FastAPI(title="EcoEncuesta API")

@app.on_event("startup")
async def startup():
    await db.connect()

@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()

@app.post("/surveys/", response_model=schemas.SurveyOut)
async def create_survey(s: schemas.SurveyCreate):
    survey = await crud.create_survey(s)
    return survey

@app.get("/surveys/{survey_id}", response_model=schemas.SurveyOut)
async def read_survey(survey_id: int):
    survey = await crud.get_survey(survey_id)
    if not survey:
        raise HTTPException(status_code=404, detail="Survey not found")
    return survey
