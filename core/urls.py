from django.urls import path
from .views import (
    home,
    dashboard,
    TrabajadorListView,
    TrabajadorCreateView,
    TrabajadorUpdateView,
    TrabajadorDeleteView,
    UnidadListView,
    UnidadCreateView,
    UnidadUpdateView,
    UnidadDeleteView,
)

urlpatterns = [
    path("", home, name="home"),
    path("dashboard/", dashboard, name="dashboard"),


    # TRABAJADORES
    path("trabajadores/", TrabajadorListView.as_view(), name="trabajador_list"),
    path("trabajadores/nuevo/", TrabajadorCreateView.as_view(), name="trabajador_create"),
    path("trabajadores/<int:pk>/editar/", TrabajadorUpdateView.as_view(), name="trabajador_edit"),
    path("trabajadores/<int:pk>/eliminar/", TrabajadorDeleteView.as_view(), name="trabajador_delete"),

    # UNIDADES
    path("unidades/", UnidadListView.as_view(), name="unidad_list"),
    path("unidades/nueva/", UnidadCreateView.as_view(), name="unidad_create"),
    path("unidades/<int:pk>/editar/", UnidadUpdateView.as_view(), name="unidad_edit"),
    path("unidades/<int:pk>/eliminar/", UnidadDeleteView.as_view(), name="unidad_delete"),


]
