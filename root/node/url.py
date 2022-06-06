from django.urls import path, include
from rest_framework.routers import DefaultRouter

from root.node.view import Convert, ConvertFromURL, Convert2, Convert3, Convert4, Convert5, Convert6

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('api/convertfile/', Convert4.as_view()),
    path('api/convertfile2/', Convert2.as_view()),
    path('api/convertfromurl/',ConvertFromURL.as_view())

]