from django.contrib import admin
from django.urls import path, re_path

from . import views
from .views import (
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete,
    category_post,
)

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name='list'),
    # path('category/', views.category_list, name='category_list'),
    path('category/<slug>/', views.category_post, name='category_post'),
    path('create/', views.post_create, name='create'),
    path('<slug>/', views.post_detail, name='detail'),
    path('<slug>/edit/', views.post_update, name='update'),
    path('<slug>/delete/', views.post_delete),
]
