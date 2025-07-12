from django.contrib import admin
from django.urls import path, include  # Include is needed to connect app-level URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('kpa.urls')),  # Connects all kpa app APIs under /api/
]
