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
    AsistenciaListView,
    AsistenciaCreateView,
    AsistenciaUpdateView,
    AsistenciaDeleteView,
     CalendarioLaboralList,
    CalendarioLaboralCreate,
    CalendarioLaboralUpdate,
    CalendarioLaboralDelete,
    IncidenciaListView,
    IncidenciaCreateView,
    IncidenciaUpdateView,
    IncidenciaDeleteView,
    marcar_entrada,
    marcar_salida,
    reporte_asistencia
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
    
    #JORNADAS
    path("jornadas/", JornadaListView.as_view(), name="jornada_list"),
    path("jornadas/nueva/", JornadaCreateView.as_view(), name="jornada_create"),
    path("jornadas/<int:pk>/editar/", JornadaUpdateView.as_view(), name="jornada_update"),
    path("jornadas/<int:pk>/eliminar/", JornadaDeleteView.as_view(), name="jornada_delete"),

    # ASISTENCIA
    path("asistencias/", AsistenciaListView.as_view(), name="asistencia_list"),
    path("asistencias/nueva/", AsistenciaCreateView.as_view(), name="asistencia_create"),
    path("asistencias/<int:pk>/editar/", AsistenciaUpdateView.as_view(), name="asistencia_edit"),
    path("asistencias/<int:pk>/eliminar/", AsistenciaDeleteView.as_view(), name="asistencia_delete"),
    path("asistencias/entrada/<int:trabajador_id>/", marcar_entrada, name="marcar_entrada"),
    path("asistencias/salida/<int:trabajador_id>/", marcar_salida, name="marcar_salida"),
    path("reportes/asistencia/", reporte_asistencia, name="reporte_asistencia"),


    # CALENDARIO LABORAL
    path("calendario/", CalendarioLaboralList.as_view(), name="calendario_laboral_list"),
    path("calendario/nuevo/", CalendarioLaboralCreate.as_view(), name="calendario_laboral_create"),
    path("calendario/<int:pk>/editar/", CalendarioLaboralUpdate.as_view(), name="calendario_laboral_update"),
    path("calendario/<int:pk>/eliminar/", CalendarioLaboralDelete.as_view(), name="calendario_laboral_delete"),

    # INCIDENCIAS
    path("incidencias/", IncidenciaListView.as_view(), name="incidencia_list"),
    path("incidencias/nueva/", IncidenciaCreateView.as_view(), name="incidencia_create"),
    path("incidencias/<int:pk>/editar/", IncidenciaUpdateView.as_view(), name="incidencia_update"),
    path("incidencias/<int:pk>/eliminar/", IncidenciaDeleteView.as_view(), name="incidencia_delete"),
]

