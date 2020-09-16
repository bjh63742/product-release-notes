from __future__ import absolute_import, unicode_literals

from django.conf.urls import url, include
from django.contrib import admin

from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^', include('product_release_notes.urls')),
    url(r'^admin/', admin.site.urls),

    url(r'^deploy-instructions/$', TemplateView.as_view(
        template_name="deploy-instructions.html"
    )),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
