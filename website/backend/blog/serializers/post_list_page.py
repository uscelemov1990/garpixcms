from rest_framework import serializers
from ..models.post_page import PostPage


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostPage
        fields = ('title', 'description', 'image', 'get_absolute_url')
