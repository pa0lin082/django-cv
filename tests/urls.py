from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from curriculum.revealjs.views import get_resume
from curriculum.views import export_single_page, export_classic

urlpatterns = [
    url(r'^revealjs/(?P<resume_id>\d*)/$', get_resume, name="reveal-js"),
    url(r'^export/(?P<resume_id>\d*)/single_page', export_single_page, name="single_page"),
    url(r'^export/(?P<resume_id>\d*)(!/classic)?', export_classic, name="classic"),
    url(r'^admin/', include(admin.site.urls)),
]    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
