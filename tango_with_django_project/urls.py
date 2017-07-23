from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.views.static import serve
from rango import views
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rango/', include('rango.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.simple.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns = urlpatterns + [
        url(r'^media/(?P<path>.*)', serve,
            {'document_root': settings.MEDIA_ROOT})
    ]
