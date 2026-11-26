# Blog de Electricidad y Magnetismo

Blog web desarrollado con Django que publica apuntes sobre Electricidad y Magnetismo, organizados por capítulo.

## Tecnologías

- Python 3
- Django 6
- SQLite
- HTML y CSS

## Funcionalidades

- Listado de posts publicados, ordenados del más nuevo al más viejo.
- Panel de administración para gestionar los posts.
- Crear, ver, editar y eliminar posts desde la web, con imagen opcional.
- Registro, inicio y cierre de sesión de usuarios.
- Las acciones de crear, editar y eliminar requieren haber iniciado sesión.

## Contenido

Apuntes elaborados en base al *Curso de Electricidad y Magnetismo* de Gerardo Pozzi, con autorización del autor. Capítulos publicados:

1. Electrostática
2. Conductores y dieléctricos
3. Corrientes estacionarias

## Instalación y ejecución

El proyecto fue desarrollado en Windows (PowerShell).

### 1. Clonar el repositorio

```
git clone https://github.com/alejandrodeutz25-DLC/Blog-Electricidad-Magnetismo.git
cd Blog-Electricidad-Magnetismo
```

### 2. Crear y activar el entorno virtual

```
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar las dependencias

```
pip install -r requirements.txt
```

### 4. Aplicar las migraciones

```
python manage.py migrate
```

### 5. Crear un superusuario

```
python manage.py createsuperuser
```

### 6. Levantar el servidor

```
python manage.py runserver
```

Abrir en el navegador:

- Sitio: http://127.0.0.1:8000/
- Panel de administración: http://127.0.0.1:8000/admin/

La base de datos y las imágenes subidas no se incluyen en el repositorio. Después de crear el superusuario, se pueden cargar posts desde el panel de administración.

## Autor

Alejandro Deutz