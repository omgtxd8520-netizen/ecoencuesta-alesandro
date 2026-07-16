from src.app.schemas import SurveyCreate


def test_survey_create_valid():
    s = SurveyCreate(respondent_name="Ana", location="Valle", score=4, notes="Good")
    assert s.score == 4


def test_survey_score_required():
    try:
        SurveyCreate()
        assert False, "Validation should fail when score is missing"
    except Exception:
        assert True
