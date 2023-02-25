from django.urls import path
from .views import get_list_of_books, delete_book, create_book

urlpatterns = [
    path('', get_list_of_books, name='books'),
    path('<int:id>/delete', delete_book, name='delete_book'),
    path('create_book/', create_book, name='create_book'),
]
