from django.db import models
from garpix_page.models import BaseListPage

from ..serializers.post_list_page import PostListSerializer

from ..models.post_page import PostPage


class PostListPage(BaseListPage):
    paginate_by = 5
    template = 'pages/post_list.html'

    def get_context(self, request=None, *args, **kwargs):
        from .tag import Tag
        from garpix_utils.paginator import GarpixPaginator
        context = super().get_context(request, *args, **kwargs)
        tags = {
            'tags': Tag.objects.values()
        }
        context.update(tags)

        try:
            page = int(request.GET.get('page', 1))
        except ValueError:
            page = 1

        object_list = self.children.filter(is_active=True)
        paginator = GarpixPaginator(object_list, self.paginate_by)
        paginated_object_list = paginator.get_page(page)
        art = {
            'list': PostListSerializer(paginated_object_list, many=True).data
        }
        context.update(art)

        return context

    class Meta:
        verbose_name = "PostList"
        verbose_name_plural = "PostLists"
        ordering = ('-created_at',)
