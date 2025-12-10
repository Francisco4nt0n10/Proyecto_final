from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import date
from django.contrib import messages

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse # Importado del lado HEAD para exportar CSV

# Se incluyen todos los modelos de ambos lados del conflicto:
from .models import Trabajador, UnidadAdministrativa, JornadaLaboral,RegistroAsistencia, CalendarioLaboral, Incidencia,TipoIncidencia,TipoNombramiento
# Se incluyen todos los formularios de ambos lados del conflicto:
from .forms import TrabajadorForm, UnidadAdministrativaForm, JornadaLaboralForm,RegistroAsistenciaForm,TipoIncidenciaForm,TipoNombramientoForm 

import csv
from datetime import datetime

# ---------- HOME / DASHBOARD ----------

def home(request):
    return render(request, "home.html")


@login_required
def dashboard(request):
    context = {"username": request.user.username}
    return render(request, "dashboard.html", context)


# ---------- TRABAJADOR ----------

class TrabajadorListView(LoginRequiredMixin, ListView):
    model = Trabajador
    template_name = "trabajador_list.html"
    context_object_name = "trabajadores"


class TrabajadorCreateView(LoginRequiredMixin, CreateView):
    model = Trabajador
    form_class = TrabajadorForm
    template_name = "trabajador_create.html"
    success_url = reverse_lazy("trabajador_list")


class TrabajadorUpdateView(LoginRequiredMixin, UpdateView):
    model = Trabajador
    form_class = TrabajadorForm
    template_name = "trabajador_create.html"
    success_url = reverse_lazy("trabajador_list")


class TrabajadorDeleteView(LoginRequiredMixin, DeleteView):
    model = Trabajador
    template_name = "trabajador_delete.html"
    success_url = reverse_lazy("trabajador_list")


# ---------- UNIDAD ADMINISTRATIVA ----------

class UnidadListView(LoginRequiredMixin, ListView):
    model = UnidadAdministrativa
    template_name = "unidad_list.html"
    context_object_name = "unidades"


class UnidadCreateView(LoginRequiredMixin, CreateView):
    model = UnidadAdministrativa
    form_class = UnidadAdministrativaForm
    template_name = "unidad_form.html"
    success_url = reverse_lazy("unidad_list")


class UnidadUpdateView(LoginRequiredMixin, UpdateView):
    model = UnidadAdministrativa
    form_class = UnidadAdministrativaForm
    template_name = "unidad_form.html"
    success_url = reverse_lazy("unidad_list")


class UnidadDeleteView(LoginRequiredMixin, DeleteView):
    model = UnidadAdministrativa
    template_name = "unidad_delete.html"
    success_url = reverse_lazy("unidad_list")


# ---------- JORNADA LABORAL ----------
class JornadaListView(LoginRequiredMixin, ListView):
    model = JornadaLaboral
    template_name = "jornada_list.html"
    context_object_name = "jornadas"


class JornadaCreateView(LoginRequiredMixin, CreateView):
    model = JornadaLaboral
    form_class = JornadaLaboralForm
    template_name = "jornada_form.html"
    success_url = reverse_lazy("jornada_list")


class JornadaUpdateView(LoginRequiredMixin, UpdateView):
    model = JornadaLaboral
    form_class = JornadaLaboralForm
    template_name = "jornada_form.html"
    success_url = reverse_lazy("jornada_list")


class JornadaDeleteView(LoginRequiredMixin, DeleteView):
    model = JornadaLaboral
    template_name = "jornada_delete.html"
    success_url = reverse_lazy("jornada_list")
    
#Registro Asistencia
class AsistenciaListView(LoginRequiredMixin, ListView):
    model = RegistroAsistencia
    template_name = "asistencia_list.html"
    context_object_name = "asistencias"


class AsistenciaDeleteView(LoginRequiredMixin, DeleteView):
    model = RegistroAsistencia
    template_name = "asistencia_delete.html"
    success_url = reverse_lazy("asistencia_list")

class AsistenciaCreateView(LoginRequiredMixin, CreateView):
    model = RegistroAsistencia
    form_class = RegistroAsistenciaForm
    template_name = "asistencia_form.html"
    success_url = reverse_lazy("asistencia_list")


class AsistenciaUpdateView(LoginRequiredMixin, UpdateView):
    model = RegistroAsistencia
    form_class = RegistroAsistenciaForm
    template_name = "asistencia_form.html"
    success_url = reverse_lazy("asistencia_list")

def marcar_salida(request, trabajador_id):
    trabajador = get_object_or_404(Trabajador, id=trabajador_id)
    hoy = date.today()

    registro = RegistroAsistencia.objects.filter(
        trabajador=trabajador,
        fecha=hoy
    ).first()

    if not registro:
        messages.error(request, "No puedes registrar salida sin entrada.")
        return redirect("asistencia_list")

    if registro.hora_salida:
        messages.error(request, "La salida ya fue registrada.")
        return redirect("asistencia_list")

    registro.hora_salida = timezone.now().time()
    registro.save()

    messages.success(request, "Salida registrada correctamente.")
    return redirect("asistencia_list")


def marcar_entrada(request, trabajador_id):
    trabajador = get_object_or_404(Trabajador, id=trabajador_id)
    hoy = date.today()

    registro, creado = RegistroAsistencia.objects.get_or_create(
        trabajador=trabajador,
        fecha=hoy,
    )

    if registro.hora_entrada:
        messages.error(request, "La entrada ya fue registrada.")
        return redirect("asistencia_list")

    registro.hora_entrada = timezone.now().time()
    registro.save()

    messages.success(request, "Entrada registrada correctamente.")
    return redirect("asistencia_list")

# ---------- Calendario Laboral ----------
class CalendarioLaboralList(ListView):
    model = CalendarioLaboral
    template_name = "calendario_laboral_list.html"
    context_object_name = "calendarios"
    ordering = ["fecha"]


class CalendarioLaboralCreate(CreateView):
    model = CalendarioLaboral
    fields = ["fecha", "es_inhabil", "descripcion"]
    template_name = "calendario_laboral_form.html"
    success_url = reverse_lazy("calendario_laboral_list")


class CalendarioLaboralUpdate(UpdateView):
    model = CalendarioLaboral
    fields = ["fecha", "es_inhabil", "descripcion"]
    template_name = "calendario_laboral_form.html"
    success_url = reverse_lazy("calendario_laboral_list")


class CalendarioLaboralDelete(DeleteView):
    model = CalendarioLaboral
    template_name = "calendario_laboral_delete.html"    
    success_url = reverse_lazy("calendario_laboral_list")


# ====== INCIDENCIAS ======

class IncidenciaListView(LoginRequiredMixin, ListView):
    model = Incidencia
    template_name = "incidencia_list.html"
    context_object_name = "incidencias"

    def get_queryset(self):
        # Para no hacer demasiadas consultas
        return (
            Incidencia.objects
            .select_related("trabajador", "tipo_incidencia", "autorizada_por")
            .order_by("-fecha_inicio")
        )


class IncidenciaCreateView(LoginRequiredMixin, CreateView):
    model = Incidencia
    fields = ["trabajador", "tipo_incidencia", "fecha_inicio", "fecha_fin", "observaciones"]
    template_name = "incidencia_form.html"
    success_url = reverse_lazy("incidencia_list")

    def form_valid(self, form):
        # El usuario logueado queda como quien autoriza
        form.instance.autorizada_por = self.request.user
        return super().form_valid(form)


class IncidenciaUpdateView(LoginRequiredMixin, UpdateView):
    model = Incidencia
    fields = ["trabajador", "tipo_incidencia", "fecha_inicio", "fecha_fin", "observaciones"]
    template_name = "incidencia_form.html"
    success_url = reverse_lazy("incidencia_list")


class IncidenciaDeleteView(LoginRequiredMixin, DeleteView):
    model = Incidencia
    template_name = "incidencia_delete.html"
    success_url = reverse_lazy("incidencia_list")



# ---------- TIPO DE INCIDENCIA ----------
class TipoIncidenciaListView(LoginRequiredMixin, ListView):
    model = TipoIncidencia
    template_name = "tipoincidencia_list.html"
    context_object_name = "tipos"



class TipoIncidenciaCreateView(LoginRequiredMixin, CreateView):
    model = TipoIncidencia
    form_class = TipoIncidenciaForm
    template_name = "tipoincidencia_form.html"
    success_url = reverse_lazy("tipoincidencia_list")

class TipoIncidenciaUpdateView(LoginRequiredMixin, UpdateView):
    model = TipoIncidencia
    form_class = TipoIncidenciaForm
    template_name = "tipoincidencia_form.html"
    success_url = reverse_lazy("tipoincidencia_list")

class TipoIncidenciaDeleteView(LoginRequiredMixin, DeleteView):
    model = TipoIncidencia
    template_name = "tipoincidencia_delete.html"
    success_url = reverse_lazy("tipoincidencia_list")

 # ---------- TIPO NOMBRAMIENTO CRUD ----------

class TipoNombramientoListView(LoginRequiredMixin, ListView):
    model = TipoNombramiento
    template_name = "tiponombramiento_list.html"
    context_object_name = "tipos"


class TipoNombramientoCreateView(LoginRequiredMixin, CreateView):
    model = TipoNombramiento
    form_class = TipoNombramientoForm
    template_name = "tiponombramiento_form.html"
    success_url = reverse_lazy("tiponombramiento_list")


class TipoNombramientoUpdateView(LoginRequiredMixin, UpdateView):
    model = TipoNombramiento
    form_class = TipoNombramientoForm
    template_name = "tiponombramiento_form.html"
    success_url = reverse_lazy("tiponombramiento_list")


class TipoNombramientoDeleteView(LoginRequiredMixin, DeleteView):
    model = TipoNombramiento
    template_name = "tiponombramiento_delete.html"
    success_url = reverse_lazy("tiponombramiento_list")
#Reportes
def reporte_asistencia(request):
    trabajadores = Trabajador.objects.all()
    unidades = UnidadAdministrativa.objects.all()

    #Obtener los filtros con el GET
    trabajador_id = request.GET.get("trabajador")
    unidad_id = request.GET.get("unidad")
    fecha_inicio = request.GET.get("fecha_inicio")
    fecha_fin = request.GET.get("fecha_fin")

    registros = RegistroAsistencia.objects.all()

    # Nota: Los filtros deben usar el nombre del campo en el modelo.
    # Asumo que el campo de relación se llama 'trabajador' y el ID de unidad
    # es accesible a través del trabajador.
    # Por favor, verifica el nombre correcto del campo de relación si falla.

    if trabajador_id:
        # Se asume que el campo en RegistroAsistencia se llama 'trabajador'
        registros = registros.filter(trabajador__id=trabajador_id) 

    if unidad_id:
        # Se asume que en el modelo Trabajador, el campo a UnidadAdministrativa se llama 'unidad'
        registros = registros.filter(trabajador__unidad__id=unidad_id) 
        # Si el campo se llama 'id_unidad' en Trabajador, el filtro sería:
        # registros = registros.filter(trabajador__id_unidad__id=unidad_id) 
        # Tu código original usaba: registros.filter(id_trabajador__id_unidad=unidad_id) - lo cambié a la convención de Django.


    if fecha_inicio:
        registros = registros.filter(fecha__gte=fecha_inicio)

    if fecha_fin:
        registros = registros.filter(fecha__lte=fecha_fin)

    #Exportación CSV
    if "export_csv" in request.GET:
        return exportar_csv(registros)

    return render(request, "reporte_asistencia.html", {
        "trabajadores": trabajadores,
        "unidades": unidades,
        "registros": registros,
    })


def exportar_csv(registros):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reporte_asistencia.csv"'

    writer = csv.writer(response)

    writer.writerow(["Trabajador", "Fecha", "Hora Entrada", "Hora Salida", "Estatus"])

    if not registros:
        writer.writerow(["SIN DATOS", "", "", "", ""])
        return response

    for r in registros:
        writer.writerow([
            r.trabajador.nombre if r.trabajador else "",
            r.fecha,
            r.hora_entrada,
            r.hora_salida,
            r.estatus,
        ])

    return response