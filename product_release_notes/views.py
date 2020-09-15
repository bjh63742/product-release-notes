from __future__ import absolute_import, unicode_literals

from django.shortcuts import render
from django.conf import settings

from .models import ReleaseNote
from .models import Client


def release_notes_list(request,client_id):
    release_notes = ReleaseNote.objects.relasedByid(client_id)

    return render(request, 'release_notes/list.html', {
        'release_notes': release_notes,
        'product_name': getattr(settings, 'RELEASE_NOTES_PRODUCT_NAME', ''),
        'page_description': getattr(settings, 'RELEASE_NOTES_PAGE_DESCRIPTION', ''),
        'embed': bool(request.GET.get('embed'))
    })

def release_notes_clients(request):
    clients = Client.objects.all()

    return render(request, 'release_notes/home.html', {
        'clients': clients
    })
