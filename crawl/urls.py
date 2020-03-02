# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('wuhan_news', views.wuhan_crawl, name='index'),
]