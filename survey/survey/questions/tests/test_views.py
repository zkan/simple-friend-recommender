from django.test import TestCase
from django.urls import reverse


class TestQuestion0View(TestCase):
    def test_question_0_view_should_have_some_random_text(self):
        url = reverse('questions:question_0')
        response = self.client.get(url)
        assert 'Question 0' in str(response.content)


class TestQuestion1View(TestCase):
    def test_question_1_view_should_have_some_random_text(self):
        url = reverse('questions:question_1')
        response = self.client.get(url)
        assert 'Question 1' in str(response.content)


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
