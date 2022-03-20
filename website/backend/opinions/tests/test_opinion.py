from ..forms.feedback import FeedbackForm
from ..models.feedback import Feedback


class OpinionFeedbackForm:
    def test_opinion(self):
        email = 'list@mail.ru'
        data = {'email': email, 'comment': 'opinion'}
        form = FeedbackForm(data=data)
        form.is_valid()
        form.save()
        assert Feedback.objects.filter(email=email).count == 1

    def test_bad(self):
        data = {'email': 'aaa', 'comment': 'opinion'}
        form = FeedbackForm(data=data)
        is_valid = form.is_valid()
        assert not is_valid
        assert 'email' in form.errors
