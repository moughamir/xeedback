from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

import session_csrf
session_csrf.monkeypatch()

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'feedapp.views.home', name='home'),
    #url(r'^blog/', include('blog.urls')),
    url(r'', include('blog.urls')),
    # url(r'^$', 'blog.views.index'),
    url(r'^_ah/', include('djangae.urls')),

    # Note that by default this is also locked down with login:admin in app.yaml
    url(r'^admin/', include(admin.site.urls)),

    url(r'^csp/', include('cspreports.urls')),

    # url(r'^auth/', include('djangae.contrib.gauth.urls')),
    url(r'^gauth/', include('djangae.contrib.gauth.urls')),
) + static(settings.MEDIA_URL, photo_root=settings.MEDIA_ROOT)
