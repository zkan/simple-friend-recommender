from django.urls import path

from survey.questions.views import Question1View


app_name = 'questions'
urlpatterns = [
    path('1/', view=Question1View.as_view(), name='question_1'),
]
