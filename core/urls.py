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
    JornadaListView,
    JornadaCreateView,
    JornadaUpdateView,
    JornadaDeleteView,
)

urlpatterns = [
    path("", home, name="home"),
    path("dashboard/", dashboard, name="dashboard"),

    path("trabajadores/", TrabajadorListView.as_view(), name="trabajador_list"),
    path("trabajadores/nuevo/", TrabajadorCreateView.as_view(), name="trabajador_create"),
    path("trabajadores/<int:pk>/editar/", TrabajadorUpdateView.as_view(), name="trabajador_edit"),
    path("trabajadores/<int:pk>/eliminar/", TrabajadorDeleteView.as_view(), name="trabajador_delete"),

    path("unidades/", UnidadListView.as_view(), name="unidad_list"),
    path("unidades/nueva/", UnidadCreateView.as_view(), name="unidad_create"),
    path("unidades/<int:pk>/editar/", UnidadUpdateView.as_view(), name="unidad_edit"),
    path("unidades/<int:pk>/eliminar/", UnidadDeleteView.as_view(), name="unidad_delete"),

    path("jornadas/", JornadaListView.as_view(), name="jornada_list"),
    path("jornadas/nueva/", JornadaCreateView.as_view(), name="jornada_create"),
    path("jornadas/<int:pk>/editar/", JornadaUpdateView.as_view(), name="jornada_update"),
    path("jornadas/<int:pk>/eliminar/", JornadaDeleteView.as_view(), name="jornada_delete"),
]

