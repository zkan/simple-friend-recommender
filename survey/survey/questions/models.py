from django.db import models


class SurveyResponse(models.Model):
    name = models.CharField(max_length=200)
    answers = models.JSONField(default={})
