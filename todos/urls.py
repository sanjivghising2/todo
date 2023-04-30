from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo, name='todo'),
    path('todosa/edit/', views.edit, name='edit'),
    path('todosa/', views.todosa, name='todos'),


]