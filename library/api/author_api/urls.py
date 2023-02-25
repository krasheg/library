from django.urls import path, include
from rest_framework import routers
from api.author_api.views import AuthorViewSet


router = routers.DefaultRouter()
router.register("", AuthorViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "api.author_api"
