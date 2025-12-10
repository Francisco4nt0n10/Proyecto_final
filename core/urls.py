from django.urls import path
from django.http import HttpResponse
from .views import (
    # Básico / Dashboard
    home,
    dashboard,

    # Trabajadores
    TrabajadorListView,
    TrabajadorCreateView,
    TrabajadorUpdateView,
    TrabajadorDeleteView,

    # Unidades
    UnidadListView,
    UnidadCreateView,
    UnidadUpdateView,
    UnidadDeleteView,

    # Jornadas
    JornadaListView,
    JornadaCreateView,
    JornadaUpdateView,
    JornadaDeleteView,

    # Asistencia
    AsistenciaListView,
    AsistenciaCreateView,
    AsistenciaUpdateView,
    AsistenciaDeleteView,
    marcar_entrada,
    marcar_salida,
    reporte_asistencia,
    asistencia_list,

    # Calendario laboral
    CalendarioLaboralList,
    CalendarioLaboralCreate,
    CalendarioLaboralUpdate,
    CalendarioLaboralDelete,

    # Incidencias
    IncidenciaListView,
    IncidenciaCreateView,
    IncidenciaUpdateView,
    IncidenciaDeleteView,

    # Tipo Incidencia
    TipoIncidenciaListView,
    TipoIncidenciaCreateView,
    TipoIncidenciaUpdateView,
    TipoIncidenciaDeleteView,
    
    TipoNombramientoListView,
    TipoNombramientoCreateView,
    TipoNombramientoUpdateView,
    TipoNombramientoDeleteView,

    PuestoListView,
    PuestoCreateView,
    PuestoUpdateView,
    PuestoDeleteView,

)

urlpatterns = [
    # Home
    path("", home, name="home"),
    path("dashboard/", dashboard, name="dashboard"),

    # Trabajadores
    path("trabajadores/", TrabajadorListView.as_view(), name="trabajador_list"),
    path("trabajadores/nuevo/", TrabajadorCreateView.as_view(), name="trabajador_create"),
    path("trabajadores/<int:pk>/editar/", TrabajadorUpdateView.as_view(), name="trabajador_edit"),
    path("trabajadores/<int:pk>/eliminar/", TrabajadorDeleteView.as_view(), name="trabajador_delete"),

    # Unidades
    path("unidades/", UnidadListView.as_view(), name="unidad_list"),
    path("unidades/nueva/", UnidadCreateView.as_view(), name="unidad_create"),
    path("unidades/<int:pk>/editar/", UnidadUpdateView.as_view(), name="unidad_edit"),
    path("unidades/<int:pk>/eliminar/", UnidadDeleteView.as_view(), name="unidad_delete"),

    # Jornadas
    path("jornadas/", JornadaListView.as_view(), name="jornada_list"),
    path("jornadas/nueva/", JornadaCreateView.as_view(), name="jornada_create"),
    path("jornadas/<int:pk>/editar/", JornadaUpdateView.as_view(), name="jornada_update"),
    path("jornadas/<int:pk>/eliminar/", JornadaDeleteView.as_view(), name="jornada_delete"),

    # Asistencia
    path("asistencias/", asistencia_list, name="asistencia_list"),
    path("asistencias/nueva/", AsistenciaCreateView.as_view(), name="asistencia_create"),
    path("asistencias/<int:pk>/editar/", AsistenciaUpdateView.as_view(), name="asistencia_edit"),
    path("asistencias/<int:pk>/eliminar/", AsistenciaDeleteView.as_view(), name="asistencia_delete"),
    path("asistencias/entrada/<int:trabajador_id>/", marcar_entrada, name="marcar_entrada"),
    path("asistencias/salida/<int:trabajador_id>/", marcar_salida, name="marcar_salida"),
    path("reportes/asistencia/", reporte_asistencia, name="reporte_asistencia"),

    # Calendario Laboral
    path("calendario/", CalendarioLaboralList.as_view(), name="calendario_laboral_list"),
    path("calendario/nuevo/", CalendarioLaboralCreate.as_view(), name="calendario_laboral_create"),
    path("calendario/<int:pk>/editar/", CalendarioLaboralUpdate.as_view(), name="calendario_laboral_update"),
    path("calendario/<int:pk>/eliminar/", CalendarioLaboralDelete.as_view(), name="calendario_laboral_delete"),

    # Incidencias
    path("incidencias/", IncidenciaListView.as_view(), name="incidencia_list"),
    path("incidencias/nueva/", IncidenciaCreateView.as_view(), name="incidencia_create"),
    path("incidencias/<int:pk>/editar/", IncidenciaUpdateView.as_view(), name="incidencia_update"),
    path("incidencias/<int:pk>/eliminar/", IncidenciaDeleteView.as_view(), name="incidencia_delete"),

    # Tipo Incidencia
    path("tipoincidencia/", TipoIncidenciaListView.as_view(), name="tipoincidencia_list"),
    path("tipoincidencia/nuevo/", TipoIncidenciaCreateView.as_view(), name="tipoincidencia_create"),
    path("tipoincidencia/<int:pk>/editar/", TipoIncidenciaUpdateView.as_view(), name="tipoincidencia_edit"),
    path("tipoincidencia/<int:pk>/eliminar/", TipoIncidenciaDeleteView.as_view(), name="tipoincidencia_delete"),
   

   # ----- Tipo Nombramiento -----
   path("tiponombramiento/", TipoNombramientoListView.as_view(), name="tiponombramiento_list"),
   path("tiponombramiento/nuevo/", TipoNombramientoCreateView.as_view(), name="tiponombramiento_create"),
   path("tiponombramiento/<int:pk>/editar/", TipoNombramientoUpdateView.as_view(), name="tiponombramiento_edit"),
   path("tiponombramiento/<int:pk>/eliminar/", TipoNombramientoDeleteView.as_view(), name="tiponombramiento_delete"),


    #PUESTO
  path("puestos/", PuestoListView.as_view(), name="puesto_list"),
  path("puestos/nuevo/", PuestoCreateView.as_view(), name="puesto_create"),
  path("puestos/<int:pk>/editar/", PuestoUpdateView.as_view(), name="puesto_update"),
  path("puestos/<int:pk>/eliminar/", PuestoDeleteView.as_view(), name="puesto_delete"),





]

