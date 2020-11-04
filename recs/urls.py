"""Defines URL patterns for recs."""

from django.urls import path

from . import views

app_name = 'recs'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
]
