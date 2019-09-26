from django.contrib import admin
from django.urls import path, re_path

from . import views
from .views import (
    PostCreateAPIView,
    PostDetailAPIView,
    PostListAPIView,
    PostDeleteAPIView,
    PostUpdateAPIView,
)

app_name = 'posts'

urlpatterns = [
    path('', PostListAPIView.as_view(), name='list'),
#     # path('category/', views.category_list, name='category_list'),
#     path('category/<slug>/', views.category_post, name='category_post'),
    path('create/', PostCreateAPIView.as_view(), name='create'),
    path('<slug>/', PostDetailAPIView.as_view(), name='detail'),
    path('<slug>/edit/', PostUpdateAPIView.as_view(), name='update'),
    path('<slug>/delete/', PostDeleteAPIView.as_view(), name='delete'),
 ]
