from django.test import TestCase
from ..models.post_page import PostPage


class PostTestCase(TestCase):
    def setUp(self):
        PostPage.objects.create(title='title', description='description', text='text')

    def valid_post(self):
        post = PostPage.objects.get(title='title')
        self.assertTrue(post)
