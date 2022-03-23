from rest_framework import serializers
from ..models.post_page import PostPage
from .tag import TagSerializer


class PostPageSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = PostPage
        fields = '__all__'
