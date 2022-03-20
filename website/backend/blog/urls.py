from rest_framework import routers
from .views.post_title import PostTitleViewSet

title_router = routers.DefaultRouter()
title_router.register(r'title', PostTitleViewSet)

urlpatterns = title_router.urls
