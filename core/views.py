from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import date
from django.contrib import messages

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Trabajador, UnidadAdministrativa, JornadaLaboral,RegistroAsistencia, CalendarioLaboral, Incidencia
from .forms import TrabajadorForm, UnidadAdministrativaForm, JornadaLaboralForm,RegistroAsistenciaForm


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