from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from garpix_page.models import BasePage
from garpix_utils.file.file_field import get_file_path

from .tag import Tag


class PostPage(BasePage):
    template = "pages/post.html"

    description = models.TextField()
    text = RichTextUploadingField(blank=True, default='', verbose_name='Содержание')
    image = models.ImageField(upload_to=get_file_path, blank=True, verbose_name='Изображение')
    tags = models.ManyToManyField(Tag, related_name='tag_posts', verbose_name='Теги')

    def get_serializer(self):
        from ..serializers import PostPageSerializer
        return PostPageSerializer

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ("-created_at",)
