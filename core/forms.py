from django import forms
from .models import Trabajador, UnidadAdministrativa, JornadaLaboral,RegistroAsistencia


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


class JornadaLaboralForm(forms.ModelForm):
    class Meta:
        model = JornadaLaboral
        fields = ["descripcion", "hora_entrada", "hora_salida", "dias_semana"]   


class RegistroAsistenciaForm(forms.ModelForm):
    class Meta:
        model = RegistroAsistencia
        fields = ["trabajador", "fecha", "hora_entrada", "hora_salida"]
