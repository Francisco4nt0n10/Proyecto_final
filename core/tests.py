from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from .models import (
    UnidadAdministrativa,
    Trabajador,
    Puesto,
    TipoNombramiento,
    JornadaLaboral,
    RegistroAsistencia
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

