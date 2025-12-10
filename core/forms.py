from django import forms
from .models import Trabajador, UnidadAdministrativa, JornadaLaboral, RegistroAsistencia, TipoIncidencia,TipoNombramiento, CalendarioLaboral, Puesto

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


class TipoIncidenciaForm(forms.ModelForm):
    class Meta:
        model = TipoIncidencia
        fields = ["nombre", "descripcion"]


class TipoNombramientoForm(forms.ModelForm):
    class Meta:
        model = TipoNombramiento
        fields = ["descripcion"]
        widgets = {
            "descripcion": forms.TextInput(attrs={
                "class": "border rounded p-2 w-full",
                "placeholder": "Descripción del nombramiento"
            })
        }



class PuestoForm(forms.ModelForm):
    class Meta:
        model = Puesto
        fields = ['nombre_puesto', 'nivel']

class CalendarioLaboralForm(forms.ModelForm):
    class Meta:
        model = CalendarioLaboral
        fields = ["fecha", "descripcion", "es_inhabil"]
        widgets = {
            "fecha": forms.DateInput(
                attrs={
                    "class": "border border-gray-300 p-2 w-full rounded-md "
                             "bg-gray-50 focus:ring-2 focus:ring-indigo-500 focus:outline-none",
                    "type": "date",
                }
            ),
            "descripcion": forms.TextInput(
                attrs={
                    "class": "border border-gray-300 p-2 w-full rounded-md "
                             "bg-gray-50 focus:ring-2 focus:ring-indigo-500 focus:outline-none",
                }
            ),
            "es_inhabil": forms.CheckboxInput(
                attrs={
                    "class": "h-4 w-4 text-indigo-600 border-gray-300 rounded focus:ring-indigo-500",
                }
            ),
        }
