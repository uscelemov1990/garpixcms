from rest_framework import serializers
from ..models.post_page import PostPage


class PostTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostPage
        fields = ('title',)
