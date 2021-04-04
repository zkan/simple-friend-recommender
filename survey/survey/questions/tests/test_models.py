from django.test import TestCase

from ..models import SurveyResponse


class TestSurveyResponse(TestCase):
    def test_survey_response_should_have_defined_fields(self):
        name = 'Kan'
        answers = {
            'question_1': 'test',
            'question_2': 'yeah'
        }
        SurveyResponse.objects.create(
            name=name,
            answers=answers
        )

        survey_response = SurveyResponse.objects.get(name=name)

        assert survey_response.name == name
        assert survey_response.answers == answers

    def test_survey_response_should_set_empty_dict_as_default_for_answers(self):
        name = 'Kan'
        SurveyResponse.objects.create(
            name=name,
        )

        survey_response = SurveyResponse.objects.get(name=name)

        assert survey_response.name == name
        assert survey_response.answers == {}
