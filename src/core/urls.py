import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap

from .sitemaps import StaticViewSitemap

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': {
        'main': StaticViewSitemap,
    }}, name="django.contrib.sitemaps.views.sitemap",),
    path('', TemplateView.as_view(template_name='core/home.html'), name='home'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
