from django.shortcuts import (
    redirect,
    render,
    reverse,
)
from django.views import View

from .models import SurveyResponse


class Question0View(View):
    template_name = 'question_0.html'

    def get(self, request):
        name = request.GET.get('name')
        if name:
            SurveyResponse.objects.get_or_create(name=name)

            return redirect(reverse('questions:question_1') + f'?name={name}')

        return render(request, self.template_name)


class Question1View(View):
    template_name = 'question_1.html'

    def get(self, request):
        name = request.GET.get('name')
        choice = request.GET.get('choice')
        if name and choice:
            survey_response, _ = SurveyResponse.objects.get_or_create(name=name)
            survey_response.answers['data-engineer'] = 1 if choice == 'data-engineer' else 0
            survey_response.answers['data-scientist'] = 1 if choice == 'data-scientist' else 0
            survey_response.save()

            return redirect('questions:question_2')

        return render(
            request,
            self.template_name,
            {
                'name': name,
            }
        )


class Question2View(View):
    template_name = 'question_2.html'

    def get(self, request):
        return render(request, self.template_name)


class Question3View(View):
    template_name = 'question_3.html'

    def get(self, request):
        return render(request, self.template_name)


class Question4View(View):
    template_name = 'question_4.html'

    def get(self, request):
        return render(request, self.template_name)


class Question5View(View):
    template_name = 'question_5.html'

    def get(self, request):
        return render(request, self.template_name)


class ThankYouView(View):
    template_name = 'thankyou.html'

    def get(self, request):
        return render(request, self.template_name)
