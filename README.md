# Proyecto Ferremas

## Configuración del Entorno Virtual (venv)

1. **Instalar `virtualenv`**:
    ```sh
    pip install virtualenv
    ```

2. **Crear y activar el entorno virtual**:
    ```sh
    virtualenv venv
    venv\Scripts\activate  # Windows
    source venv/bin/activate  # macOS y Linux
    ```

3. **Instalar dependencias**:
    ```sh
    pip install -r requirements.txt
    ```

## Cargar Datos en la Base de Datos (SQLite3)

1. **Aplicar migraciones y cargar datos**:
    ```sh
    python manage.py migrate
    python manage.py loaddata data.json
    ```

Esto configurará y poblará tu base de datos con los datos iniciales.

## Levantar el Servidor

Para iniciar el servidor, usa:
```sh
py manage.py runserver
```