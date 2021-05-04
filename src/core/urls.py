from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('inside/', admin.site.urls),
]
