from rest_framework import routers
from .views.opinions import OpinionsViewSet

opinion_router = routers.DefaultRouter()
opinion_router.register(r'opinion', OpinionsViewSet)

urlpatterns = opinion_router.urls
