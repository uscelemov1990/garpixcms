from rest_framework import viewsets

from ..serializers.post_title import PostTitleSerializer
from ..models import PostPage


class PostTitleViewSet(viewsets.ModelViewSet):
    queryset = PostPage.objects.all()
    serializer_class = PostTitleSerializer
