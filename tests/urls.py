from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static


urlpatterns = patterns(
    '',
    url(r'^export/(?P<resume_id>\d*)', 'curriculum.views.export_resume', name="export_resume"),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
