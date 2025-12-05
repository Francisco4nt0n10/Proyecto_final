from django import forms
from .models import Trabajador, UnidadAdministrativa


class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = [
            "numero_empleado",
            "nombre",
            "apellido_paterno",
            "apellido_materno",
            "rfc",
            "curp",
            "unidad_administrativa",
            "puesto",
            "tipo_nombramiento",
            "activo",
        ]


class UnidadAdministrativaForm(forms.ModelForm):
    class Meta:
        model = UnidadAdministrativa
        fields = [
            "nombre",
            "descripcion",
            "unidad_padre",
        ]