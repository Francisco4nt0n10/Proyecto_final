from django.contrib import admin
from django.urls import path, include  # <--- 1. ¡IMPORTANTE: AGREGA 'include'!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), # <--- 2. ESTA ES LA LÍNEA MÁGICA
]