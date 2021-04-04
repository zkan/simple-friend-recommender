from django.test import TestCase
from django.urls import reverse


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


class TestQuestion1View(TestCase):
    def test_question_1_view_should_have_some_random_text(self):
        url = reverse('questions:question_1')
        response = self.client.get(url)
        assert 'Question 1' in str(response.content)
        assert 'Question 1 <a href="?choice=1">Hhhhh</a><a href="?choice=2">WWWW</a>' in str(response.content)


class TestQuestion2View(TestCase):
    def test_question_2_view_should_have_some_random_text(self):
        url = reverse('questions:question_2')
        response = self.client.get(url)
        assert 'Question 2' in str(response.content)


class TestQuestion3View(TestCase):
    def test_question_3_view_should_have_some_random_text(self):
        url = reverse('questions:question_3')
        response = self.client.get(url)
        assert 'Question 3' in str(response.content)


class TestQuestion4View(TestCase):
    def test_question_4_view_should_have_some_random_text(self):
        url = reverse('questions:question_4')
        response = self.client.get(url)
        assert 'Question 4' in str(response.content)


class TestQuestion5View(TestCase):
    def test_question_5_view_should_have_some_random_text(self):
        url = reverse('questions:question_5')
        response = self.client.get(url)
        assert 'Question 5' in str(response.content)
