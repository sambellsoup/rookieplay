"""Defines URL patterns for recs."""

from django.urls import path

from . import views

app_name = 'recs'
urlpatterns = [
    # Home Page
    # path('', views.index, name='index'),

    path('', views.upload, name='upload'),

    # Show all topics.
    path('topics/', views.topics, name='topics'),

    #Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    #Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),

    path('new_entry/<int:topic_id/', views.new_entry, name='new_entry'),

    #Page for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
