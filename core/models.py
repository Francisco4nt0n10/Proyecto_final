from django.db import models
from django.contrib.auth.models import User

# Modelo Trabajador
class Trabajador(models.Model):
    numero_empleado = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    rfc = models.CharField(max_length=13)
    curp = models.CharField(max_length=18)
    unidad_administrativa = models.ForeignKey('UnidadAdministrativa', on_delete=models.CASCADE)
    puesto = models.ForeignKey('Puesto', on_delete=models.CASCADE)
    tipo_nombramiento = models.ForeignKey('TipoNombramiento', on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"

# Modelo UnidadAdministrativa
class UnidadAdministrativa(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    unidad_padre = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre

# Modelo Puesto
class Puesto(models.Model):
    nombre_puesto = models.CharField(max_length=100)
    nivel = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_puesto

# Modelo TipoNombramiento
class TipoNombramiento(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

# Modelo JornadaLaboral
class JornadaLaboral(models.Model):
    descripcion = models.CharField(max_length=100)
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField()
    dias_semana = models.CharField(max_length=50)  # L-V (lunes a viernes)

    def __str__(self):
        return self.descripcion

# Modelo CalendarioLaboral
class CalendarioLaboral(models.Model):
    fecha = models.DateField()
    es_inhabil = models.BooleanField(default=False)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.fecha} - {self.descripcion}"

# Modelo TrabajadorJornada
class TrabajadorJornada(models.Model):
    trabajador = models.ForeignKey('Trabajador', on_delete=models.CASCADE)
    jornada = models.ForeignKey('JornadaLaboral', on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.trabajador} - {self.jornada}"

        
# Modelo Registro Asistencia
class RegistroAsistencia(models.Model):
    trabajador = models.ForeignKey('Trabajador', on_delete=models.CASCADE)
    fecha = models.DateField()

    hora_entrada = models.TimeField(null=True, blank=True)
    hora_salida = models.TimeField(null=True, blank=True)

    estatus = models.CharField(max_length=50, default="Pendiente")

    def calcular_estatus(self):
        """Evalúa la asistencia según la jornada asignada."""
        jornada = self.trabajador.jornada  # Asegúrate de que trabajador tenga FK a JornadaLaboral

        if not self.hora_entrada:
            self.estatus = "Falta"
            return

        # RETARDO
        if self.hora_entrada > jornada.hora_entrada:
            self.estatus = "Retardo"
        else:
            self.estatus = "Asistencia normal"

    def save(self, *args, **kwargs):
        if self.hora_entrada:
            self.calcular_estatus()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Asistencia de {self.trabajador} - {self.fecha}"
# Modelo TipoIncidencia
class TipoIncidencia(models.Model):
    nombre = models.CharField(max_length=100, default="Incidencia")
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre



# Modelo Incidencia
class Incidencia(models.Model):
    trabajador = models.ForeignKey('Trabajador', on_delete=models.CASCADE)
    tipo_incidencia = models.ForeignKey('TipoIncidencia', on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    observaciones = models.TextField()
    autorizada_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Incidencia de {self.trabajador} - {self.tipo_incidencia}"

# Modelo PerfilUsuario
class PerfilUsuario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trabajador = models.ForeignKey('Trabajador', on_delete=models.SET_NULL, null=True, blank=True)
    rol = models.CharField(max_length=50, choices=[('Administrador', 'Administrador'), ('Jefe', 'Jefe'), ('Trabajador', 'Trabajador')])

    def __str__(self):
        return f"Perfil de {self.user.username} - {self.rol}"