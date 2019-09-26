from django.contrib import admin
from django.urls import path, re_path

from . import views
from .views import (
    UserCreateAPIView,
    UserLoginAPIView,
)

app_name = 'comments'

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
]
