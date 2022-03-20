from rest_framework import viewsets

from ..serializers.feedback import FeedbackSerializer
from ..models import Feedback


class OpinionsViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
