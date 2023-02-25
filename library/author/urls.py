from django.urls import path
from .views import AuthorsList, delete_author,create_author

urlpatterns = [
    path('', AuthorsList.as_view(), name='authors'),
    path('<int:id>/delete', delete_author, name='delete_author'),
    path('create_author', create_author, name='create_author'),
]
