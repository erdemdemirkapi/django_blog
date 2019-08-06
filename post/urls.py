from django.urls import path
from post.views import *

from . import views

app_name = 'post'

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),

    path('index/', post_index, name = 'index'),
    path('create/', post_create, name = 'create'),
    path('<str:slug>/', post_detail, name = 'detail'),
    path('<str:slug>/update/', post_update, name = 'update'),
    path('<str:slug>/delete/', post_delete, name = 'delete'),
]
