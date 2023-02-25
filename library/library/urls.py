"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from .views import IndexView
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from authentication.views import login_,register
from django.urls import path, include, re_path
from authentication.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_, name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('register/', register, name='register'),
    path('authors/', include('author.urls')),
    path('', IndexView.as_view(), name='index'),
    path('users/', include('authentication.urls')),
    path('book/', include('book.urls')),
    path('order/', include('order.urls'), name='order'),
    # api
    path('api/v1/user/', include('api.authentication_api.urls')),
    path('api/v1/order/', include('api.order_api.urls')),

    path('api/v1/author/', include('api.author_api.urls')),
    path('api/v1/book/', include('api.book_api.urls')),
]
