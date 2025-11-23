from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # La URL de la raíz (/) ahora apunta a la app 'core'
    path('', include('core.urls')), 
    
    # URL de administración
    path('admin/', admin.site.urls),
    
    # URLs de autenticación (login, logout, signup)
    path('accounts/', include('allauth.urls')), 
]