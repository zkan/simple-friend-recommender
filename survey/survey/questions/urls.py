from django.urls import path

from survey.questions.views import (
    Question0View,
    Question1View,
)


app_name = 'questions'
urlpatterns = [
    path('0/', view=Question0View.as_view(), name='question_0'),
    path('1/', view=Question1View.as_view(), name='question_1'),
]
