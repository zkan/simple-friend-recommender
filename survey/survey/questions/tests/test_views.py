from django.test import TestCase
from django.urls import reverse

from ..models import SurveyResponse


class TestQuestion0View(TestCase):
    def setUp(self):
        self.url = reverse('questions:question_0')

    def test_question_0_view_should_have_title(self):
        response = self.client.get(self.url)
        assert '<title>Question 0</title>' in str(response.content)

    def test_question_0_view_should_have_form_for_submitting_name(self):
        response = self.client.get(self.url)
        expected = '<form action="." method="GET">' \
            '<div class="mb-3">' \
            '<label for="name" class="form-label">Name</label>' \
            '<input id="name" type="text" class="form-control" name="name" />' \
            '</div>' \
            '<button type="submit" class="btn btn-primary">Submit</button>' \
            '</form>'
        assert expected in str(response.content)

    def test_question_0_view_should_redirect_when_input_name(self):
        name = 'Kan'
        response = self.client.get(self.url + f'?name={name}')

        assert response.status_code == 302

    def test_question_0_view_should_redirect_to_question_1_when_input_name(self):
        name = 'Kan'
        response = self.client.get(self.url + f'?name={name}', follow=True)

        assert '<title>Question 1</title>' in str(response.content)

    def test_question_0_view_should_save_name_when_input_name(self):
        name = 'Kan'
        self.client.get(self.url + f'?name={name}')

        survey_response = SurveyResponse.objects.get(name=name)
        assert survey_response.name == name
        assert survey_response.answers == {}

    def test_question_0_view_should_get_or_create_name_when_input_same_name(self):
        name = 'Kan'
        SurveyResponse.objects.create(
            name=name,
            answers={}
        )

        self.client.get(self.url + f'?name={name}')

        survey_response = SurveyResponse.objects.filter(name=name)

        assert survey_response.count() == 1


class TestQuestion1View(TestCase):
    def setUp(self):
        self.url = reverse('questions:question_1')

    def test_question_1_view_should_have_title(self):
        response = self.client.get(self.url)
        assert '<title>Question 1</title>' in str(response.content)

    def test_question_1_view_should_show_data_engineer_vs_data_scientist(self):
        name = 'zkan'
        response = self.client.get(self.url + f'?name={name}')

        data_engineer_card = f'<a href="?name={name}&choice=data-engineer">' \
            '<div class="card border-light">' \
            '<img src="/static/data-engineer.png" class="card-img-top">' \
            '<div class="card-body text-center">' \
            '<h5 class="card-title">Data Engineer</h5>' \
            '</div>' \
            '</div>' \
            '</a>'
        assert data_engineer_card in str(response.content)

        data_scientist_card = f'<a href="?name={name}&choice=data-scientist">' \
            '<div class="card border-light">' \
            '<img src="/static/data-scientist.png" class="card-img-top">' \
            '<div class="card-body text-center">' \
            '<h5 class="card-title">Data Scientist</h5>' \
            '</div>' \
            '</div>' \
            '</a>'
        assert data_scientist_card in str(response.content)

    def test_question_1_view_should_save_data_engineer_answer_for_responder(self):
        name = 'Kan'
        choice = 'data-engineer'
        SurveyResponse.objects.create(
            name=name,
            answers={}
        )
        self.client.get(self.url + f'?name={name}&choice={choice}')

        survey_response = SurveyResponse.objects.get(name=name)
        assert survey_response.name == name

        expected = {
            'question-1': 'data-engineer',
        }
        assert survey_response.answers == expected

    def test_question_1_view_should_save_data_scientist_answer_for_responder(self):
        name = 'Kan'
        choice = 'data-scientist'
        SurveyResponse.objects.create(
            name=name,
            answers={}
        )
        self.client.get(self.url + f'?name={name}&choice={choice}')

        survey_response = SurveyResponse.objects.get(name=name)
        assert survey_response.name == name

        expected = {
            'question-1': 'data-scientist',
        }
        assert survey_response.answers == expected

    def test_question_1_view_should_redirect_when_input(self):
        name = 'Kan'
        choice = 'data-engineer'
        SurveyResponse.objects.create(
            name=name,
            answers={}
        )
        response = self.client.get(self.url + f'?name={name}&choice={choice}')

        assert response.status_code == 302

    def test_question_1_view_should_redirect_to_question_2_when_input(self):
        name = 'Kan'
        choice = 'data-engineer'
        SurveyResponse.objects.create(
            name=name,
            answers={}
        )
        response = self.client.get(self.url + f'?name={name}&choice={choice}', follow=True)

        assert '<title>Question 2</title>' in str(response.content)


class TestQuestion2View(TestCase):
    def setUp(self):
        self.url = reverse('questions:question_2')

    def test_question_2_view_should_have_title(self):
        response = self.client.get(self.url)
        assert '<title>Question 2</title>' in str(response.content)

    def test_question_2_view_should_show_cat_vs_dog(self):
        name = 'zkan'
        response = self.client.get(self.url + f'?name={name}')

        cat_card = f'<a href="?name={name}&choice=cat">' \
            '<div class="card border-light">' \
            '<img src="/static/cat.png" class="card-img-top">' \
            '<div class="card-body text-center">' \
            '<h5 class="card-title">Cat</h5>' \
            '</div>' \
            '</div>' \
            '</a>'
        assert cat_card in str(response.content)

        dog_card = f'<a href="?name={name}&choice=dog">' \
            '<div class="card border-light">' \
            '<img src="/static/dog.png" class="card-img-top">' \
            '<div class="card-body text-center">' \
            '<h5 class="card-title">Dog</h5>' \
            '</div>' \
            '</div>' \
            '</a>'
        assert dog_card in str(response.content)

    def test_question_2_view_should_save_cat_answer_for_responder(self):
        name = 'Kan'
        choice = 'cat'
        SurveyResponse.objects.create(
            name=name,
            answers={}
        )
        self.client.get(self.url + f'?name={name}&choice={choice}')

        survey_response = SurveyResponse.objects.get(name=name)
        assert survey_response.name == name

        expected = {
            'question-2': 'cat',
        }
        assert survey_response.answers == expected

    def test_question_2_view_should_save_data_scientist_answer_for_responder(self):
        name = 'Kan'
        choice = 'dog'
        SurveyResponse.objects.create(
            name=name,
            answers={}
        )
        self.client.get(self.url + f'?name={name}&choice={choice}')

        survey_response = SurveyResponse.objects.get(name=name)
        assert survey_response.name == name

        expected = {
            'question-2': 'dog',
        }
        assert survey_response.answers == expected

    def test_question_2_view_should_redirect_when_input(self):
        name = 'Kan'
        choice = 'cat'
        SurveyResponse.objects.create(
            name=name,
            answers={}
        )
        response = self.client.get(self.url + f'?name={name}&choice={choice}')

        assert response.status_code == 302

    def test_question_2_view_should_redirect_to_question_3_when_input(self):
        name = 'Kan'
        choice = 'cat'
        SurveyResponse.objects.create(
            name=name,
            answers={}
        )
        response = self.client.get(self.url + f'?name={name}&choice={choice}', follow=True)

        assert '<title>Question 3</title>' in str(response.content)


class TestQuestion3View(TestCase):
    def setUp(self):
        self.url = reverse('questions:question_3')

    def test_question_3_view_should_have_title(self):
        response = self.client.get(self.url)
        assert '<title>Question 3</title>' in str(response.content)

    def test_question_3_view_should_show_sea_vs_mountain(self):
        name = 'zkan'
        response = self.client.get(self.url + f'?name={name}')

        sea_card = f'<a href="?name={name}&choice=sea">' \
            '<div class="card border-light">' \
            '<img src="/static/sea.png" class="card-img-top">' \
            '<div class="card-body text-center">' \
            '<h5 class="card-title">Sea</h5>' \
            '</div>' \
            '</div>' \
            '</a>'
        assert sea_card in str(response.content)

        mountain_card = f'<a href="?name={name}&choice=mountain">' \
            '<div class="card border-light">' \
            '<img src="/static/mountain.png" class="card-img-top">' \
            '<div class="card-body text-center">' \
            '<h5 class="card-title">Mountain</h5>' \
            '</div>' \
            '</div>' \
            '</a>'
        assert mountain_card in str(response.content)

    def test_question_3_view_should_save_sea_answer_for_responder(self):
        name = 'Kan'
        choice = 'sea'
        SurveyResponse.objects.create(
            name=name,
            answers={}
        )
        self.client.get(self.url + f'?name={name}&choice={choice}')

        survey_response = SurveyResponse.objects.get(name=name)
        assert survey_response.name == name

        expected = {
            'question-3': 'sea',
        }
        assert survey_response.answers == expected

    def test_question_3_view_should_save_mountain_answer_for_responder(self):
        name = 'Kan'
        choice = 'mountain'
        SurveyResponse.objects.create(
            name=name,
            answers={}
        )
        self.client.get(self.url + f'?name={name}&choice={choice}')

        survey_response = SurveyResponse.objects.get(name=name)
        assert survey_response.name == name

        expected = {
            'question-3': 'mountain',
        }
        assert survey_response.answers == expected

    def test_question_3_view_should_redirect_when_input(self):
        name = 'Kan'
        choice = 'sea'
        SurveyResponse.objects.create(
            name=name,
            answers={}
        )
        response = self.client.get(self.url + f'?name={name}&choice={choice}')

        assert response.status_code == 302

    def test_question_3_view_should_redirect_to_question_3_when_input(self):
        name = 'Kan'
        choice = 'sea'
        SurveyResponse.objects.create(
            name=name,
            answers={}
        )
        response = self.client.get(self.url + f'?name={name}&choice={choice}', follow=True)

        assert '<title>Question 4</title>' in str(response.content)


class TestQuestion4View(TestCase):
    def setUp(self):
        self.url = reverse('questions:question_4')

    def test_question_4_view_should_have_title(self):
        response = self.client.get(self.url)
        assert '<title>Question 4</title>' in str(response.content)

    def test_question_4_view_should_show_python_vs_java(self):
        name = 'zkan'
        response = self.client.get(self.url + f'?name={name}')

        python_card = f'<a href="?name={name}&choice=python">' \
            '<div class="card border-light">' \
            '<img src="/static/python.png" class="card-img-top">' \
            '<div class="card-body text-center">' \
            '<h5 class="card-title">Python</h5>' \
            '</div>' \
            '</div>' \
            '</a>'
        assert python_card in str(response.content)

        java_card = f'<a href="?name={name}&choice=java">' \
            '<div class="card border-light">' \
            '<img src="/static/java.png" class="card-img-top">' \
            '<div class="card-body text-center">' \
            '<h5 class="card-title">Java</h5>' \
            '</div>' \
            '</div>' \
            '</a>'
        assert java_card in str(response.content)

    def test_question_4_view_should_save_python_answer_for_responder(self):
        name = 'Kan'
        choice = 'python'
        SurveyResponse.objects.create(
            name=name,
            answers={}
        )
        self.client.get(self.url + f'?name={name}&choice={choice}')

        survey_response = SurveyResponse.objects.get(name=name)
        assert survey_response.name == name

        expected = {
            'question-4': 'python',
        }
        assert survey_response.answers == expected

    def test_question_4_view_should_save_java_answer_for_responder(self):
        name = 'Kan'
        choice = 'java'
        SurveyResponse.objects.create(
            name=name,
            answers={}
        )
        self.client.get(self.url + f'?name={name}&choice={choice}')

        survey_response = SurveyResponse.objects.get(name=name)
        assert survey_response.name == name

        expected = {
            'question-4': 'java',
        }
        assert survey_response.answers == expected

    def test_question_4_view_should_redirect_when_input(self):
        name = 'Kan'
        choice = 'python'
        SurveyResponse.objects.create(
            name=name,
            answers={}
        )
        response = self.client.get(self.url + f'?name={name}&choice={choice}')

        assert response.status_code == 302

    def test_question_4_view_should_redirect_to_question_5_when_input(self):
        name = 'Kan'
        choice = 'python'
        SurveyResponse.objects.create(
            name=name,
            answers={}
        )
        response = self.client.get(self.url + f'?name={name}&choice={choice}', follow=True)

        assert '<title>Question 5</title>' in str(response.content)


class TestQuestion5View(TestCase):
    def test_question_5_view_should_have_title(self):
        url = reverse('questions:question_5')
        response = self.client.get(url)
        assert '<title>Question 5</title>' in str(response.content)


class TestThankYouView(TestCase):
    def test_thank_you_view_should_have_title(self):
        url = reverse('questions:thankyou')
        response = self.client.get(url)
        assert '<title>Thank You</title>' in str(response.content)
