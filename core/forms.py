from django import forms
from .models import Trabajador, UnidadAdministrativa, JornadaLaboral, RegistroAsistencia, TipoIncidencia,TipoNombramiento

# Define las clases base de Tailwind para todos los inputs
TAILWIND_INPUT_CLASSES = 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2 focus:ring-indigo-500 focus:border-indigo-500'
TAILWIND_CHECKBOX_CLASSES = 'rounded border-gray-300 text-indigo-600 shadow-sm focus:ring-indigo-500' # Para campos booleanos

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
        # Aplica estilos a los campos de TrabajadorForm
        widgets = {
            "numero_empleado": forms.TextInput(attrs={'class': TAILWIND_INPUT_CLASSES}),
            "nombre": forms.TextInput(attrs={'class': TAILWIND_INPUT_CLASSES}),
            "apellido_paterno": forms.TextInput(attrs={'class': TAILWIND_INPUT_CLASSES}),
            "apellido_materno": forms.TextInput(attrs={'class': TAILWIND_INPUT_CLASSES}),
            "rfc": forms.TextInput(attrs={'class': TAILWIND_INPUT_CLASSES}),
            "curp": forms.TextInput(attrs={'class': TAILWIND_INPUT_CLASSES}),
            "unidad_administrativa": forms.Select(attrs={'class': TAILWIND_INPUT_CLASSES}),
            "puesto": forms.TextInput(attrs={'class': TAILWIND_INPUT_CLASSES}),
            "tipo_nombramiento": forms.Select(attrs={'class': TAILWIND_INPUT_CLASSES}),
            "activo": forms.CheckboxInput(attrs={'class': TAILWIND_CHECKBOX_CLASSES}),
        }


class UnidadAdministrativaForm(forms.ModelForm):
    class Meta:
        model = UnidadAdministrativa
        fields = [
            "nombre",
            "descripcion",
            "unidad_padre",
        ]
        # Aplica estilos a los campos de UnidadAdministrativaForm
        widgets = {
            "nombre": forms.TextInput(attrs={'class': TAILWIND_INPUT_CLASSES}),
            "descripcion": forms.Textarea(attrs={'class': TAILWIND_INPUT_CLASSES, 'rows': 3}),
            "unidad_padre": forms.Select(attrs={'class': TAILWIND_INPUT_CLASSES}),
        }


class JornadaLaboralForm(forms.ModelForm):
    class Meta:
        model = JornadaLaboral
        fields = ["descripcion", "hora_entrada", "hora_salida", "dias_semana"]  
        
        widgets = {
            "descripcion": forms.TextInput(attrs={'class': TAILWIND_INPUT_CLASSES}),
            "hora_entrada": forms.TimeInput(attrs={'class': TAILWIND_INPUT_CLASSES, 'type': 'time'}),
            "hora_salida": forms.TimeInput(attrs={'class': TAILWIND_INPUT_CLASSES, 'type': 'time'}),
            
            # 🎯 MODIFICACIÓN CLAVE: Cambiamos de SelectMultiple a CheckboxSelectMultiple
            # para una mejor visualización y usabilidad.
            "dias_semana": forms.CheckboxSelectMultiple(attrs={
                # Dejamos la clase vacía. El diseño visual (columnas)
                # se maneja directamente en la plantilla HTML.
                'class': '' 
            }),
        }


class RegistroAsistenciaForm(forms.ModelForm):
    class Meta:
        model = RegistroAsistencia
        fields = ["trabajador", "fecha", "hora_entrada", "hora_salida"]
        # Aplica estilos a los campos de RegistroAsistenciaForm
        widgets = {
            "trabajador": forms.Select(attrs={'class': TAILWIND_INPUT_CLASSES}),
            "fecha": forms.DateInput(attrs={'class': TAILWIND_INPUT_CLASSES, 'type': 'date'}),
            "hora_entrada": forms.TimeInput(attrs={'class': TAILWIND_INPUT_CLASSES, 'type': 'time'}),
            "hora_salida": forms.TimeInput(attrs={'class': TAILWIND_INPUT_CLASSES, 'type': 'time'}),
        }


class TipoIncidenciaForm(forms.ModelForm):
    class Meta:
        model = TipoIncidencia
        fields = ["nombre", "descripcion"]
        # Aplica estilos a los campos de TipoIncidenciaForm
        widgets = {
            "nombre": forms.TextInput(attrs={'class': TAILWIND_INPUT_CLASSES}),
            "descripcion": forms.Textarea(attrs={'class': TAILWIND_INPUT_CLASSES, 'rows': 3}),
        }


class TipoNombramientoForm(forms.ModelForm):
    class Meta:
        model = TipoNombramiento
        fields = ["descripcion"]
        widgets = {
            # Se mantiene el estilo que tenías, pero usando la clase definida
            "descripcion": forms.TextInput(attrs={
                "class": TAILWIND_INPUT_CLASSES, # Usamos la clase general
                "placeholder": "Descripción del nombramiento"
            })
        }