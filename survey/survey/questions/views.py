from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class Question0View(View):
    def get(self, request):
        return HttpResponse('Question 0')


class Question1View(View):
    def get(self, request):
        return HttpResponse('Question 1')


class Question2View(View):
    def get(self, request):
        return HttpResponse('Question 2')


class Question3View(View):
    def get(self, request):
        return HttpResponse('Question 3')


class Question4View(View):
    def get(self, request):
        return HttpResponse('Question 4')


class Question5View(View):
    def get(self, request):
        return HttpResponse('Question 5')
