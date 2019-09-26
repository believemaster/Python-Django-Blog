from django.contrib import admin
from django.urls import path, re_path

from . import views
from .views import (
	comment_thread,
    comment_delete,
)

app_name = 'comments'

urlpatterns = [
    path('<id>/', views.comment_thread, name='thread'),
    path('<id>/delete/', views.comment_delete, name='delete'),
]
