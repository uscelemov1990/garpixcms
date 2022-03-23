from django.test import TestCase
from ..models.feedback import Feedback


class OpinionFeedbackForm(TestCase):
    def setUp(self):
        Feedback.objects.create(email='list@mail.ru', comment='opinion')

    def test_valid_post(self):
        feedback = Feedback.objects.get(email='list@mail.ru')
        self.assertTrue(feedback)
