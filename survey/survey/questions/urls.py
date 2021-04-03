from django.urls import path

from survey.questions.views import (
    Question0View,
    Question1View,
    Question2View,
    Question3View,
    Question4View,
    Question5View,
)


app_name = 'questions'
urlpatterns = [
    path('0/', view=Question0View.as_view(), name='question_0'),
    path('1/', view=Question1View.as_view(), name='question_1'),
    path('2/', view=Question2View.as_view(), name='question_2'),
    path('3/', view=Question3View.as_view(), name='question_3'),
    path('4/', view=Question4View.as_view(), name='question_4'),
    path('5/', view=Question5View.as_view(), name='question_5'),
]
