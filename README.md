# Proyecto_Coderhouse

**Alumno:** Andrea Rivera

## Descripción

Este proyecto es una aplicación web desarrollada con Django, es una simulacion de un tienda de vinilos.

El proyecto utiliza el patrón MVT (Modelo-Vista-Template) de Django y hace uso de la herencia de plantillas para mantener un diseño consistente en las diferentes páginas. Además, se ha creado un superusuario para facilitar la administración de la aplicación.

## Funcionalidades actuales

1. **Registro de usuario**: Los usuarios pueden registrarse en el sistema (proximamente iniciar sesion).
2. **Agregar discos**: Se puede agregar discos a la base de datos, incluyendo la opción de marcar cuáles serán destacados. (solo admin)
3. **Buscar discos**: Se puede realizar una búsqueda por discos a través del buscador de la página.
4. **Navegación básica**: La página incluye enlaces para navegar entre diferentes secciones (aunque algunos botones aún no están funcionando completamente).
5. **Superusuario**: Se ha configurado un superusuario para facilitar la administración del sistema.

   - **Usuario**: admin
   - **Contraseña**: 123

## Instrucciones para ejecutar el proyecto

1. Clonar el repositorio en tu máquina local:
   git clone <URL_DEL_REPOSITORIO>


Navegar al directorio del proyecto:
Copiar código
cd Proyecto_Coderhouse

Crear un entorno virtual:
Copiar código
python -m venv venv


Activar el entorno virtual:

En Windows:
Copiar código
venv\Scripts\activate

En Mac/Linux:
Copiar código
source venv/bin/activate

Instalar las dependencias del proyecto:
Copiar código
pip install -r requirements.txt

Realizar las migraciones de la base de datos:
Copiar código
python manage.py migrate

Crear un superusuario para acceder al panel de administración:
Copiar código
python manage.py createsuperuser

Ejecutar el servidor de desarrollo:
Copiar código
python manage.py runserver
El proyecto estará disponible en: http://127.0.0.1:8000/

## Rutas principales
Página principal: Muestra los discos y permite buscar discos.
Formulario de registro: Permite a los usuarios registrarse en el sistema.
Formulario de agregar disco: Permite agregar nuevos discos a la base de datos y marcar discos como destacados.
Búsqueda de discos: Los usuarios pueden buscar discos por título u otros criterios.

## Funcionalidades por completar
Algunos botones de la aplicación no están completamente implementados, pero se espera que en futuras actualizaciones, las funcionalidades de selección de discos destacados y otros botones adicionales estén habilitados.

## Notas
Los usuarios pueden acceder al panel de administración utilizando el superusuario:
Usuario: admin
Contraseña: 123
URL del panel de administración: http://127.0.0.1:8000/admin/

## Tecnologías utilizadas
Django
HTML, Bootstrap (para el diseño)
Base de datos SQLite (por defecto)

## Agradecimientos
Gracias a Coderhouse por el material de aprendizaje que hizo posible este proyecto.