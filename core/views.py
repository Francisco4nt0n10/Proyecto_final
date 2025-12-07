from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Trabajador, UnidadAdministrativa, JornadaLaboral
from .forms import TrabajadorForm, UnidadAdministrativaForm, JornadaLaboralForm


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
