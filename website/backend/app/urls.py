from garpixcms.urls import *  # noqa

urlpatterns = [
                  path('api/v1/opinions/', include('opinions.urls')),
                  path('api/v1/post/', include('blog.urls')),
                  path('api/v1/user/', include('user.urls')),
              ] + urlpatterns  # noqa
