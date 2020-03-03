# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('chat/lobby', views.index, name='index'),
]
