from __future__ import absolute_import, unicode_literals

from django.urls import path

from .views import release_notes_list
from .views import pdf
from .views import release_notes_clients
from .feed import ReleaseNotesFeed

urlpatterns = [
    path('', release_notes_clients),
    path('<int:client_id>', release_notes_list),
    path('pdf/<int:client_id>', pdf),
    path('feed', ReleaseNotesFeed(), name='release-notes-feed'),
]
