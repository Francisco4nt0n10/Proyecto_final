from django.urls import path
from . import views

# Definición del nombre de la aplicación para usarla en las plantillas (por ejemplo: core:dashboard)
app_name = 'core'

urlpatterns = [
    # Ruta de inicio: '/'
    path('', views.home, name='home'),
    
    # Ruta del panel de control: '/dashboard/'
    path('dashboard/', views.dashboard, name='dashboard'),
    

]