from django.contrib import admin
from django.urls import path, include

from root import settings

urlpatterns = [
    path('', include('root.node.url')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),

                  ] + urlpatterns
