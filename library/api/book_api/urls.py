from django.urls import path, include
from rest_framework import routers
from api.book_api.views import BookViewSet


router = routers.DefaultRouter()
router.register("", BookViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "api.book_api"
