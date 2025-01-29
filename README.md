# Proyecto_Coderhouse

**Alumno:** Andrea Rivera

## Descripción

Este proyecto es una aplicación web desarrollada con Django, es una simulación de una un buscador de vinilos donde puedes ver el precio aproximado y lo que contiene.

El proyecto utiliza el patrón MVT (Modelo-Vista-Template) de Django y hace uso de la herencia de plantillas para mantener un diseño consistente en las diferentes páginas. Además, se ha creado un superusuario para facilitar la administración de la aplicación.

## Funcionalidades

- **Inicio**: Página principal del buscador.
- **Acerca de mí**: Página de contacto con información sobre el dueño.
- **Catálogo**: Listado de discos disponibles.
- **Detalle de Disco**: Vista detallada de cada disco.
- **Registro de Usuario**: Formulario para registrar nuevos usuarios.
- **Inicio de Sesión**: Formulario para iniciar sesión.
- **Perfil de Usuario**: Vista y edición del perfil de usuario.
- **Mensajería**: Funcionalidad para enviar y recibir mensajes entre usuarios.
- **CRUD de Páginas**: Crear, editar y eliminar.

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/Proyecto_Coderhouse.git
   cd Proyecto_Coderhouse

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: .\.venv\Scripts\activate

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt

4. Realiza las migraciones:
   ```bash
   python manage.py migrate

5. Crea un superusuario:
   ```bash
   python manage.py createsuperuser

6. Ejecuta el servidor de desarrollo:
   ```bash
   python manage.py runserver

7. Accede a la aplicación en tu navegador:

## Rutas principales
- **Página principal**: Muestra los discos y permite buscar discos.
- **Formulario de registro**: Permite a los usuarios registrarse en el sistema.
- **Formulario de agregar disco**: Permite agregar nuevos discos a la base de datos y    marcar discos como destacados.
- **Búsqueda de discos**: Los usuarios pueden buscar discos por título u otros criterios.
- **Perfil de usuario**: Permite a los usuarios ver y editar su perfil.
- **Acerca de mi**: Muestra mis contactos

## Notas
   Los usuarios pueden acceder al panel de administración utilizando el superusuario:

   - **Usuario**: admin
   - **Contraseña**: 123
   - **URL del panel de administración**: http://127.0.0.1:8000/admin/

## Tecnologías utilizadas
   Django
   HTML, Bootstrap (para el diseño)
   Base de datos SQLite (por defecto)

# Agradecimientos
Gracias a Coderhouse por el material de aprendizaje que hizo posible este proyecto.