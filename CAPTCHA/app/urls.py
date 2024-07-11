import imp
from django.urls import path
from app import views

urlpatterns = [
    path('', views.puzzle, name='puzzle'),
]