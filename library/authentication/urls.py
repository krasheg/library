from django.urls import path
from authentication.views import *

urlpatterns = [
    path('', get_users, name='users'),
    path('login', login_, name='login'),
    path('register', register, name='register'),
    path('details/<int:id>', get_user_details, name='user'),
    path('delete/<int:id>', delete_user, name='delete'),
    path('update/<int:id>', update_user, name='update'),
    path('save/<int:id>', save_user, name='save')
]
