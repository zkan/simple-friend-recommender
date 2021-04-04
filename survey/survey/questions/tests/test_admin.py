from django.contrib import admin
from django.test import TestCase

from ..admin import SurveyResponseAdmin
from ..models import SurveyResponse


class TestSurveyResponseAdmin(TestCase):
    def test_admin_should_be_registered(self):
        assert isinstance(admin.site._registry[SurveyResponse], SurveyResponseAdmin)

    def test_admin_should_set_list_display(self):
        expected = (
            'name',
            'answers',
        )
        assert SurveyResponseAdmin.list_display == expected
