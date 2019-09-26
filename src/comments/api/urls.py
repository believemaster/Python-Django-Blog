from django.contrib import admin
from django.urls import path, re_path

from . import views
from .views import (
    CommentCreateAPIView,
    CommentListAPIView,
    CommentDetailAPIView,
)

app_name = 'comments'

urlpatterns = [
    path('', CommentListAPIView.as_view(), name='list'),
    path('create/', CommentCreateAPIView.as_view(), name='create'),
    path('<id>/', CommentDetailAPIView.as_view(), name='thread'),
    # path('<id>/delete/', views.comment_delete, name='delete'),
]
