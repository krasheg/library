from django.urls import path
from order.views import order, delete_order, create, complete


urlpatterns = [
    path('', order, name='orders'),
    path('<int:id>/delete', delete_order, name='delete_order'),
    path('create/', create, name='create'),
    path('<int:id>/complete', complete, name='complete'),
]
