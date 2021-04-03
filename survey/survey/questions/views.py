from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class Question1View(View):
    def get(self, request):
        return HttpResponse('Question 1')
