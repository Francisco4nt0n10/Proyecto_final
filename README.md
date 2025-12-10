# Sistema de Control de Asistencia (S.C.A.)

Este proyecto es un sistema de gestión web diseñado para registrar, monitorear y administrar de forma eficiente la asistencia del personal en una organización. Utiliza la tecnología Django con una interfaz moderna basada en Tailwind CSS.

Características Principales:
-Registro de Asistencia: Permite registrar entradas y salidas de forma precisa.
-Gestión de Empleados: Módulo completo para administrar datos personales y laborales de cada trabajador.
-Definición de Jornadas: Permite crear jornadas laborales personalizadas (horarios, días laborables) y asignarlas a los empleados.
-Control de Incidencias: Registro y seguimiento de retardos, ausencias, permisos y otros tipos de incidencias.
-Unidades Administrativas: Estructura jerárquica para organizar a los empleados por departamentos o unidades.

 # Tecnologías Utilizadas
 
 BackendPython3.xLenguaje de programación principal.
 FrameworkDjango4.x/5.x
 Base de DatosSQLite/PostgreSQLN/
 FrontendHTML5, JavaScriptN/A
 Estructura y lógica del lado del cliente.
 Estilos CSS
 Tailwind CSS3
 .xFramework CSS utility-first 
 
 # Guía de Instalación y Ejecución
 Sigue estos pasos para configurar y ejecutar el proyecto localmente.
 
 Prerrequisitos Asegúrate de tener instalado:
 Python 3.xGitInstalación
 
Clonar el repositorio: git clone https://github.com/Francisco4nt0n10/Proyecto_final.git
cd Proyecto_final

Crear y activar el entorno virtual (venv):Bash# En Windows
python -m venv venv
.\venv\Scripts\activate

En macOS/Linux
python3 -m venv venv
source venv/bin/activate

Instalar dependencias de Python:
Bashpip install -r requirements.txt

Configurar la base de datos y migrar:
Bash python manage.py makemigrations
python manage.py migrate

Crear un superusuario (Administrador):
Bashpython manage.py createsuperuser

Ejecución del Servidor
Ejecutar el servidor de Django:
python manage.py runserver
Abre tu navegador y navega a http://127.0.0.1:8000/



# Contribución
Si deseas contribuir a este proyecto, sigue estos pasos:Haz un Fork (bifurcación) del repositorio.

Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).

Realiza tus cambios y haz commit (git commit -m 'feat: Añadir nueva funcionalidad X').

Sube tus cambios a tu repositorio bifurcado (git push origin feature/nueva-funcionalidad).
Abre un Pull Request (Solicitud de Extracción) a la rama main o develop del repositorio original.


# Equipo y Contacto
NombreContactoDesarrolladores Principal
Mariela 
Alexis
Carolina


# Licencia 
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
