from __future__ import absolute_import, unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

from .models import ReleaseNote
from .models import Client

import pdfkit

def release_notes_list(request,client_id):
    release_notes = ReleaseNote.objects.relasedByid(client_id)
    client = Client.objects.filter(id=client_id)
    print(client[0].name)

    return render(request, 'release_notes/list.html', {
        'appName': client[0].name,
        'appID': client_id,
        'release_notes': release_notes,
        'product_name': getattr(settings, 'RELEASE_NOTES_PRODUCT_NAME', ''),
        'embed': bool(request.GET.get('embed'))
    })

def pdf(request, client_id):
    
    # Create a URL of our project and go to the template route
    projectUrl = request.get_host() + '/'+str(client_id)
    print(projectUrl)
    pdf = pdfkit.from_url(projectUrl, False)
    client = Client.objects.filter(id=client_id)
    # Generate download
    response = HttpResponse(pdf,content_type='application/pdf')
    fileName = "attachment; filename="+client[0].name+"Release Notes.pdf";
    response['Content-Disposition'] = fileName.encode('utf-8')

    return response


def release_notes_clients(request):
    clients = Client.objects.all()

    return render(request, 'release_notes/home.html', {
        'clients': clients
    })
