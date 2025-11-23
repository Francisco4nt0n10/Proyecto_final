from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Vista para la página principal (Home)
# Será la página de aterrizaje antes de iniciar sesión.
def home(request):
    """Renderiza la plantilla de inicio (landing page)."""
    return render(request, 'home.html')

# Vista para el Panel de Control (Dashboard)
# El decorador @login_required garantiza que solo los usuarios autenticados
# puedan acceder a esta página. Si no están logueados, serán redirigidos al login.
@login_required
def dashboard(request):
    """Renderiza el panel de control del usuario autenticado."""
    # Aquí podríamos pasar datos del usuario o estadísticas
    context = {
        'username': request.user.username,
    }
    return render(request, 'dashboard.html')