# posts/urls.py
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index,),
    # Страница с публикциями
    path('posts/', views.posts,),
    # Страница с сообществами
    path('group/<slug:slug>/', views.group_posts,),
]
