from django.urls import path, include
from .views import OrderApiView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', OrderApiView)

urlpatterns = [
    path('', include(router.urls)),
]
