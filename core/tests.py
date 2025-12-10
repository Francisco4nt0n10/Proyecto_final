from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

from .models import (
    UnidadAdministrativa,
    Trabajador,
    Puesto,
    TipoNombramiento,
    JornadaLaboral,
    RegistroAsistencia,
    CalendarioLaboral,
<<<<<<< HEAD
    TipoIncidencia,
    Incidencia,
=======
    TipoIncidencia
>>>>>>> AbrilDiaz
)


class BaseTestCase(TestCase):
    """
    Clase base para reutilizar setup:
    - Crea usuario
    - Crea cliente logueado
    """

    def setUp(self):
        self.clientDjango = Client()
        self.user = User.objects.create_user(
            username="testuser",
            password="12345"
        )
        # login
        self.clientDjango.login(username="testuser", password="12345")


#   PRUEBAS UNIDAD ADMINISTRATIVA
class UnidadAdministrativaTests(BaseTestCase):

    def test_unidad_list_view_requires_login(self):
        clientAnon = Client()
        response = clientAnon.get(reverse("unidad_list"))
        # login_required redirige (302) a página de login
        self.assertEqual(response.status_code, 302)

    def test_unidad_list_view_ok(self):
        response = self.clientDjango.get(reverse("unidad_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "unidad_list.html")

    def test_unidad_create_view_crea_unidad(self):
        data = {
            "nombre": "Administración",
            "descripcion": "Área administrativa",
            "unidad_padre": "",
        }
        response = self.clientDjango.post(reverse("unidad_create"), data)
        # Debe redirigir después de crear (302)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(UnidadAdministrativa.objects.count(), 1)
        unidad = UnidadAdministrativa.objects.first()
        self.assertEqual(unidad.nombre, "Administración")

    def test_unidad_edit_view_actualiza_unidad(self):
        unidad = UnidadAdministrativa.objects.create(
            nombre="Recursos Humanos",
            descripcion="RH",
        )

        data = {
            "nombre": "RH Modificado",
            "descripcion": "Área modificada",
            "unidad_padre": "",
        }
        response = self.clientDjango.post(
            reverse("unidad_edit", args=[unidad.id]),
            data,
        )
        self.assertEqual(response.status_code, 302)
        unidad.refresh_from_db()
        self.assertEqual(unidad.nombre, "RH Modificado")
        self.assertEqual(unidad.descripcion, "Área modificada")

    def test_unidad_delete_view_elimina_unidad(self):
        unidad = UnidadAdministrativa.objects.create(
            nombre="Contabilidad",
            descripcion="Área contable",
        )
        self.assertEqual(UnidadAdministrativa.objects.count(), 1)

        response = self.clientDjango.post(
            reverse("unidad_delete", args=[unidad.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(UnidadAdministrativa.objects.count(), 0)


#   PRUEBAS TRABAJADOR
class TrabajadorTests(BaseTestCase):

    def setUp(self):
        super().setUp()

        # Datos base necesarios para Trabajador
        self.unidad = UnidadAdministrativa.objects.create(
            nombre="Unidad Principal",
            descripcion="Unidad base para pruebas",
        )
        self.puesto = Puesto.objects.create(
            nombre_puesto="Docente",
            nivel="A"
        )
        self.tipoNombramiento = TipoNombramiento.objects.create(
            descripcion="Base"
        )

    def test_trabajador_list_view_requires_login(self):
        clientAnon = Client()
        response = clientAnon.get(reverse("trabajador_list"))
        self.assertEqual(response.status_code, 302)

    def test_trabajador_list_view_ok(self):
        response = self.clientDjango.get(reverse("trabajador_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "trabajador_list.html")

    def test_trabajador_create_view_crea_trabajador(self):
        data = {
            "numero_empleado": "12345",
            "nombre": "Juan",
            "apellido_paterno": "Pérez",
            "apellido_materno": "Gómez",
            "rfc": "PEHJ900101XXX",
            "curp": "PEHJ900101HDFXXX07",
            "unidad_administrativa": self.unidad.id,
            "puesto": self.puesto.id,
            "tipo_nombramiento": self.tipoNombramiento.id,
            "activo": True,
        }

        response = self.clientDjango.post(
            reverse("trabajador_create"),
            data,
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Trabajador.objects.count(), 1)

        trabajador = Trabajador.objects.first()
        self.assertEqual(trabajador.numero_empleado, "12345")
        self.assertEqual(trabajador.nombre, "Juan")
        self.assertTrue(trabajador.activo)

    def test_trabajador_edit_view_actualiza_trabajador(self):
        trabajador = Trabajador.objects.create(
            numero_empleado="99999",
            nombre="María",
            apellido_paterno="López",
            apellido_materno="Ramírez",
            rfc="MALR900101XXX",
            curp="MALR900101MDFXXX08",
            unidad_administrativa=self.unidad,
            puesto=self.puesto,
            tipo_nombramiento=self.tipoNombramiento,
            activo=True,
        )

        data = {
            "numero_empleado": "99999",
            "nombre": "María Editada",
            "apellido_paterno": "López",
            "apellido_materno": "Ramírez",
            "rfc": "MALR900101XXX",
            "curp": "MALR900101MDFXXX08",
            "unidad_administrativa": self.unidad.id,
            "puesto": self.puesto.id,
            "tipo_nombramiento": self.tipoNombramiento.id,
            "activo": False,
        }

        response = self.clientDjango.post(
            reverse("trabajador_edit", args=[trabajador.id]),
            data,
        )
        self.assertEqual(response.status_code, 302)

        trabajador.refresh_from_db()
        self.assertEqual(trabajador.nombre, "María Editada")
        self.assertFalse(trabajador.activo)

    def test_trabajador_delete_view_elimina_trabajador(self):
        trabajador = Trabajador.objects.create(
            numero_empleado="77777",
            nombre="Carlos",
            apellido_paterno="Sánchez",
            apellido_materno="Díaz",
            rfc="CASD900101XXX",
            curp="CASD900101HDFXXX09",
            unidad_administrativa=self.unidad,
            puesto=self.puesto,
            tipo_nombramiento=self.tipoNombramiento,
            activo=True,
        )
        self.assertEqual(Trabajador.objects.count(), 1)

        response = self.clientDjango.post(
            reverse("trabajador_delete", args=[trabajador.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Trabajador.objects.count(), 0)

#   PRUEBAS JORNADAS
class JornadaLaboralTests(TestCase):

    def setUp(self):
        # Crear usuario para autenticación
        self.user = User.objects.create_user(
            username="testuser",
            password="pass1234"
        )

        # Crear una jornada de prueba
        self.jornada = JornadaLaboral.objects.create(
            descripcion="Jornada Matutina",
            hora_entrada="08:00",
            hora_salida="14:00",
            dias_semana="L-V"
        )

    def test_jornada_list_view(self):
      
        self.client.login(username="testuser", password="pass1234")

        url = reverse("jornada_list")   # <-- corregido
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Jornada Matutina")
        self.assertTemplateUsed(response, "jornada_list.html")

    def test_jornada_create_view(self):
     
        self.client.login(username="testuser", password="pass1234")

        url = reverse("jornada_create")   # <-- corregido
        data = {
            "descripcion": "Jornada Vespertina",
            "hora_entrada": "14:00",
            "hora_salida": "20:00",
            "dias_semana": "L-V"
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # redirección

        self.assertTrue(JornadaLaboral.objects.filter(
            descripcion="Jornada Vespertina"
        ).exists())

    def test_jornada_update_view(self):
      
        self.client.login(username="testuser", password="pass1234")

        url = reverse("jornada_update", args=[self.jornada.id])   # <-- corregido

        data = {
            "descripcion": "Jornada Matutina Actualizada",
            "hora_entrada": "08:00",
            "hora_salida": "15:00",
            "dias_semana": "L-V"
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

        self.jornada.refresh_from_db()
        self.assertEqual(self.jornada.descripcion, "Jornada Matutina Actualizada")

    def test_jornada_delete_view(self):
       
        self.client.login(username="testuser", password="pass1234")

        url = reverse("jornada_delete", args=[self.jornada.id])   # <-- corregido
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.assertFalse(JornadaLaboral.objects.filter(id=self.jornada.id).exists())

 
#   PRUEBAS REGISTRO DE ASISTENCIA
# ---------------------------------------------------------
class AsistenciaTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="pass1234"
        )

        # Crear TipoNombramiento válido
        self.tipoNombramiento = TipoNombramiento.objects.create(
            descripcion="Base"
        )

        # Crear trabajador válido con ForeignKey reales
        self.trabajador = Trabajador.objects.create(
            nombre="Juan Pérez",
            apellido_paterno="Pérez",
            apellido_materno="Ramírez",
            rfc="JUAP800101XXX",
            curp="JUAP800101HDFRRN01",
            numero_empleado="123",
            tipo_nombramiento=self.tipoNombramiento,   
        )


class CalendarioLaboralViewsTests(TestCase):
    def setUp(self):
        # Un registro de ejemplo para usar en list / update / delete
        self.dia = CalendarioLaboral.objects.create(
            fecha=date(2025, 1, 15),
            es_inhabil=True,
            descripcion="Día de prueba inhábil",
        )

    # ---------- LISTA ----------

    def test_lista_usa_template_correcto(self):
        url = reverse("calendario_laboral_list")
        respuesta = self.client.get(url)

        self.assertEqual(respuesta.status_code, 200)
        self.assertTemplateUsed(respuesta, "calendario_laboral_list.html")

    def test_lista_muestra_registros(self):
        url = reverse("calendario_laboral_list")
        respuesta = self.client.get(url)

        # Debe aparecer la descripción del día creado en setUp
        self.assertContains(respuesta, "Día de prueba inhábil")

    # ---------- CREAR ----------

    def test_crear_usa_template_correcto(self):
        url = reverse("calendario_laboral_create")
        respuesta = self.client.get(url)

        self.assertEqual(respuesta.status_code, 200)
        self.assertTemplateUsed(respuesta, "calendario_laboral_form.html")

    def test_crear_registro_calendario(self):
        url = reverse("calendario_laboral_create")
        datos = {
            "fecha": "2025-02-01",
            "es_inhabil": False,
            "descripcion": "Día laborable de prueba",
        }
        respuesta = self.client.post(url, datos)

        # Debe redirigir al listado
        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(
            respuesta.url,
            reverse("calendario_laboral_list"),
        )

        # Se creó el registro en la BD
        self.assertTrue(
            CalendarioLaboral.objects.filter(
                fecha="2025-02-01", descripcion="Día laborable de prueba"
            ).exists()
        )

    # ---------- EDITAR ----------

    def test_editar_usa_template_correcto(self):
        url = reverse("calendario_laboral_update", args=[self.dia.id])
        respuesta = self.client.get(url)

        self.assertEqual(respuesta.status_code, 200)
        self.assertTemplateUsed(respuesta, "calendario_laboral_form.html")

    def test_editar_registro_calendario(self):
        url = reverse("calendario_laboral_update", args=[self.dia.id])
        datos = {
            "fecha": self.dia.fecha,
            "es_inhabil": False,
            "descripcion": "Día modificado",
        }
        respuesta = self.client.post(url, datos)

        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(
            respuesta.url,
            reverse("calendario_laboral_list"),
        )

        self.dia.refresh_from_db()
        self.assertEqual(self.dia.descripcion, "Día modificado")
        self.assertFalse(self.dia.es_inhabil)

    # ---------- ELIMINAR ----------

    def test_eliminar_usa_template_correcto(self):
        url = reverse("calendario_laboral_delete", args=[self.dia.id])
        respuesta = self.client.get(url)

        self.assertEqual(respuesta.status_code, 200)
        self.assertTemplateUsed(respuesta, "calendario_laboral_delete.html")

    def test_eliminar_registro_calendario(self):
        url = reverse("calendario_laboral_delete", args=[self.dia.id])
        respuesta = self.client.post(url)

        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(
            respuesta.url,
            reverse("calendario_laboral_list"),
        )

        # El registro ya no debe existir
        self.assertFalse(
            CalendarioLaboral.objects.filter(id=self.dia.id).exists()
        )
# -------------------------------------------------------------------
#   PRUEBAS INCIDENCIAS
# -------------------------------------------------------------------

class IncidenciaTests(BaseTestCase):

    def setUp(self):
        super().setUp()

        self.unidad = UnidadAdministrativa.objects.create(
            nombre="Unidad Pruebas",
            descripcion="Unidad para incidencias",
        )
        self.puesto = Puesto.objects.create(
            nombre_puesto="Analista",
            nivel="A1",
        )
        self.tipoNombramiento = TipoNombramiento.objects.create(
            descripcion="Base",
        )

        self.trabajador = Trabajador.objects.create(
            numero_empleado="INC001",
            nombre="Luis",
            apellido_paterno="García",
            apellido_materno="López",
            rfc="GALL900101XXX",
            curp="GALL900101HDFXXX01",
            unidad_administrativa=self.unidad,
            puesto=self.puesto,
            tipo_nombramiento=self.tipoNombramiento,
            activo=True,
        )

        self.tipoIncidencia = TipoIncidencia.objects.create(
            descripcion="Falta"
        )

    def test_incidencia_list_requires_login(self):
        clienteAnon = Client()
        respuesta = clienteAnon.get(reverse("incidencia_list"))
        self.assertEqual(respuesta.status_code, 302)

    def test_incidencia_list_ok(self):
        respuesta = self.clientDjango.get(reverse("incidencia_list"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertTemplateUsed(respuesta, "incidencia_list.html")

    def test_incidencia_create_crea_registro(self):
        datos = {
            "trabajador": self.trabajador.id,
            "tipo_incidencia": self.tipoIncidencia.id,
            "fecha_inicio": "2025-01-10",
            "fecha_fin": "2025-01-10",
            "observaciones": "Falta injustificada",
        }

        respuesta = self.clientDjango.post(
            reverse("incidencia_create"),
            datos,
        )

        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(Incidencia.objects.count(), 1)

        incidencia = Incidencia.objects.first()
        self.assertEqual(incidencia.trabajador, self.trabajador)
        self.assertEqual(incidencia.tipo_incidencia, self.tipoIncidencia)
        self.assertEqual(incidencia.observaciones, "Falta injustificada")
        self.assertEqual(incidencia.autorizada_por, self.user)

    def test_incidencia_update_actualiza_registro(self):
        incidencia = Incidencia.objects.create(
            trabajador=self.trabajador,
            tipo_incidencia=self.tipoIncidencia,
            fecha_inicio="2025-01-15",
            fecha_fin="2025-01-15",
            observaciones="Permiso personal",
            autorizada_por=self.user,
        )

        datos = {
            "trabajador": self.trabajador.id,
            "tipo_incidencia": self.tipoIncidencia.id,
            "fecha_inicio": "2025-01-15",
            "fecha_fin": "2025-01-16",
            "observaciones": "Permiso actualizado",
        }

        respuesta = self.clientDjango.post(
            reverse("incidencia_update", args=[incidencia.id]),
            datos,
        )
        self.assertEqual(respuesta.status_code, 302)

        incidencia.refresh_from_db()
        self.assertEqual(incidencia.observaciones, "Permiso actualizado")
        self.assertEqual(str(incidencia.fecha_fin), "2025-01-16")

    def test_incidencia_delete_elimina_registro(self):
        incidencia = Incidencia.objects.create(
            trabajador=self.trabajador,
            tipo_incidencia=self.tipoIncidencia,
            fecha_inicio="2025-02-01",
            fecha_fin="2025-02-01",
            observaciones="Incapacidad",
            autorizada_por=self.user,
        )
        self.assertEqual(Incidencia.objects.count(), 1)

        respuesta = self.clientDjango.post(
            reverse("incidencia_delete", args=[incidencia.id])
        )

        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(Incidencia.objects.count(), 0)



# -------------------------------------------------------------------
#   PRUEBAS TIPO INCIDENCIA
# -------------------------------------------------------------------

class TipoIncidenciaTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user("test", password="12345")
        self.client.login(username="test", password="12345")
        self.item = TipoIncidencia.objects.create(
            nombre="Permiso",
            descripcion="Personal"
        )

    def test_list(self):
        response = self.client.get(reverse("tipoincidencia_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Permiso")

    def test_create(self):
        self.client.post(reverse("tipoincidencia_create"), {
            "nombre": "Incapacidad",
            "descripcion": "Médica"
        })
        self.assertEqual(TipoIncidencia.objects.count(), 2)

    def test_edit(self):
        self.client.post(reverse("tipoincidencia_edit", args=[self.item.id]), {
            "nombre": "Modificado",
            "descripcion": "Cambio"
        })
        self.item.refresh_from_db()
        self.assertEqual(self.item.nombre, "Modificado")

    def test_delete(self):
        self.client.post(reverse("tipoincidencia_delete", args=[self.item.id]))
        self.assertEqual(TipoIncidencia.objects.count(), 0)



# -------------------------------------------------------------------
#   PRUEBAS TIPO NOMBRAMIENTO
# -------------------------------------------------------------------

class TipoNombramientoTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user("tester", password="12345")
        self.client.login(username="tester", password="12345")
        self.item = TipoNombramiento.objects.create(descripcion="Base")

    def test_list_view(self):
        response = self.client.get(reverse("tiponombramiento_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Base")

    def test_create(self):
        self.client.post(reverse("tiponombramiento_create"), {
            "descripcion": "Temporal"
        })
        self.assertEqual(TipoNombramiento.objects.count(), 2)

    def test_update(self):
        self.client.post(reverse("tiponombramiento_edit", args=[self.item.id]), {
            "descripcion": "Actualizado"
        })
        self.item.refresh_from_db()
        self.assertEqual(self.item.descripcion, "Actualizado")

    def test_delete(self):
        self.client.post(reverse("tiponombramiento_delete", args=[self.item.id]))
        self.assertEqual(TipoNombramiento.objects.count(), 0)
