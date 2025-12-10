# Sistema de Control de Asistencia (S.C.A.)

Este proyecto es un sistema de gestión web diseñado para registrar, monitorear y administrar de forma eficiente la asistencia del personal en una organización. Utiliza la tecnología Django con una interfaz moderna basada en Tailwind CSS.

##  Características Principales

**Registro de Asistencia:** Entradas y salidas (manual o simulado) y cálculo automático de retardos y faltas.

**Gestión de Incidencias:** Administración de permisos, incapacidades, comisiones (sindical/académica).

**Gestión de Personal:** Alta, baja lógica y edición de trabajadores (nombre, RFC, CURP, nombramiento, etc.).

**Organización:** Gestión de unidades administrativas (departamentos/áreas) definición de jornadas laborales y calendarios (días inhábiles).

**Roles y Permisos:** Sistema robusto de autenticación y gestión de usuarios (django-allauth) con roles de 
**Administrador**, **Jefe de Área/Supervisor** y **Trabajador**.

**Reportes:** Generación de reportes exportables  por periodo, trabajador o unidad administrativa.

]**Auditoría Básica:** Registro de creación y modificación de registros clave.


 # Tecnologías Utilizadas
 
| Componente | Tecnología | Versión | Descripción |
| :--- | :--- | :--- | :--- |
| **Backend** | Python | 3.x | Lenguaje de programación principal. |
| **Framework** | Django | 4.x/5.x | Framework web de alto nivel. |
| **Autenticación** | **django-allauth** | N/A | [cite_start]Sistema de autenticación y gestión de usuarios[cite: 19, 34]. |
| **Base de Datos** | **PostgreSQL** | N/A | [cite_start]Base de datos relacional robusta (Requisito del proyecto)[cite: 22]. |
| **Contenedores** | **Docker** y **Docker Compose** | 29.1.1 | [cite_start]Para la contenerización y orquestación de servicios (web, db)[cite: 22, 67, 68]. |
| **Frontend** | HTML5, JavaScript | N/A | Estructura y lógica del lado del cliente. |
| **Estilos CSS** | **Tailwind CSS** | 3.x | [cite_start]Framework CSS utility-first para una interfaz responsiva[cite: 71]. |
| **Control de Versiones** | **Git** | N/A | [cite_start]Para el flujo de desarrollo colaborativo[cite: 20, 72]. |
 
 # Guía de Instalación y Ejecución
 Sigue estos pasos para configurar y ejecutar el proyecto localmente.
 
 Prerrequisitos Asegúrate de tener instalado:
 Python 3.xGitInstalación
 
1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/Francisco4nt0n10/Proyecto_final.git](https://github.com/Francisco4nt0n10/Proyecto_final.git)
    cd Proyecto_final
    ```
    
2.  **Crear y activar el entorno virtual (venv):Bash# En Windows
python -m venv venv
.\venv\Scripts\activate

En macOS/Linux
python3 -m venv venv
source venv/bin/activate

3.  **Construir y Levantar los Contenedores:**
    Este comando construirá las imágenes necesarias y levantará los servicios (web/Django y db/PostgreSQL)[cite: 69].
    ```bash
    docker compose up -d --build
    ```

4.  **Instalar dependencias de Python:
Bashpip install -r requirements.txt


5.  **Ejecutar Migraciones:**
    Una vez que los servicios estén levantados, debes ejecutar las migraciones dentro del contenedor web para crear la estructura de la base de datos[cite: 43, 73].
    ```bash
    docker compose exec web python manage.py migrate
    ```

6.  **Crear un Superusuario (Administrador):**
Bashpython manage.py createsuperuser


7.  **Acceso al Sistema:**
Ejecutar el servidor de Django:
python manage.py runserver
Abre tu navegador y navega a http://127.0.0.1:8000/


## Control de Versiones y Colaboración

El proyecto sigue un flujo de desarrollo colaborativo con control de versiones consistente.

**Ramas:** Utilizamos al menos tres ramas principales (`main`, `develop`, y ramas de funcionalidad/feature).

**Flujo de Trabajo:** La integración de cambios se realiza exclusivamente mediante **Pull Requests** (PRs) para garantizar la revisión de código.

**Tags/Releases:** Se utilizan tags o releases para identificar puntos clave de la versión.

**v0.1-auth-prototype:** Prototipo funcional de autenticación con `django-allauth`[cite: 40, 124].

**v0.2-core-model:** Modelo de datos central implementado.
  
**Mensajes de Commit:** Los commits son frecuentes y tienen mensajes **descriptivos** que explican la intención del cambio.


# Contribución
Si deseas contribuir a este proyecto, sigue estos pasos:Haz un Fork (bifurcación) del repositorio.

Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).

Realiza tus cambios y haz commit (git commit -m 'feat: Añadir nueva funcionalidad X').

Sube tus cambios a tu repositorio bifurcado (git push origin feature/nueva-funcionalidad).
Abre un Pull Request (Solicitud de Extracción) a la rama main o develop del repositorio original.

### **Puntos clave agregados:**

1.  **Enfoque en Docker/Docker Compose:** Se cambiaron los pasos de instalación locales por los de **Docker Compose**, incluyendo comandos `docker compose up -d --build`, `docker compose exec web python manage.py migrate`, y `docker compose exec web python manage.py createsuperuser`.

 
2.  **Variables de Entorno:** Se agregó la instrucción para el archivo `.env`.

   
3.  **Tecnologías Clave:** Se destacaron **`PostgreSQL`**, **`django-allauth`** , **`Docker/Docker Compose`** , y **`Git`** en la tabla de tecnologías.

  
4.  **Control de Versiones:** Se detallaron los requisitos de Git: uso de **ramas** [cite: 120], **Pull Requests** , y ejemplos de **tags/releases**.

   
5.  **Requisitos Funcionales:** Se usaron los puntos del documento para hacer más detallada la sección de **Características Principales** (e.g., "Apartado B, Artículo 123", roles, reportes por periodo, etc.).


# Equipo y Contacto

| Rol | Nombre | Contacto |
| :--- | :--- | :--- |
| Desarrollador  | Mariela Sarahi Zepeda Baltazar | (L21200625@cdguzman.tecnm.com) |
| Desarrollador | Alexis Eleazar Munguia Guzman | (L20290855@cdguzman.tecnm.com) | 
| Desarrollador | Abril Carolina Diaz Magaña| (L19290628@cdguzman.tecnm.com) | 
| Desarrollador | Francisco Antonio Arce Morfin| (L2029xxxxx@cdguzman.tecnm.com) | 

# Licencia 
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
