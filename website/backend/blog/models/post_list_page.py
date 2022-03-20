from django.db import models
from garpix_page.models import BaseListPage


class PostListPage(BaseListPage):
    paginate_by = 5
    template = 'pages/post_list.html'

    def get_context(self, request=None, *args, **kwargs):
        from .tag import Tag
        context = super().get_context(request, *args, **kwargs)
        tags = {
            'tags': Tag.objects.values()
        }
        context.update(tags)
        return context

    class Meta:
        verbose_name = "PostList"
        verbose_name_plural = "PostLists"
        ordering = ('-created_at',)
