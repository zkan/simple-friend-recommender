from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View


class Question0View(View):
    template_name = 'question_0.html'

    def get(self, request):
        name = request.GET.get('name')
        if name:
            return redirect('questions:question_1')

        return render(request, self.template_name)


class Question1View(View):
    template_name = 'question_1.html'

    def get(self, request):
        choice = request.GET.get('choice')
        if choice:
            return redirect('questions:question_2')

        return render(request, self.template_name)


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
