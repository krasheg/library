from django.urls import path, include
from .views import UserApiView, OrderAPIView
from rest_framework import routers

user_router = routers.DefaultRouter()
user_router.register('', UserApiView)
order_router = routers.DefaultRouter()
order_router.register('', OrderAPIView, basename='order')

urlpatterns = [
    path('<int:user_id>/order/', include(order_router.urls)),
    path('', include(user_router.urls)),

]
