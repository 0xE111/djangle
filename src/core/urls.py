from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='core/home.html'), name='home'),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('inside/', admin.site.urls),
]
