# Proyecto Ferremas

## Configuración del Entorno Virtual (venv)

### Crear y Activar un Entorno Virtual

1. **Instalar `virtualenv`**:
    ```sh
    pip install virtualenv
    ```

2. **Crear el entorno virtual**:
    ```sh
    virtualenv venv
    ```

3. **Activar el entorno virtual**:
    - **Windows**:
        ```sh
        venv\Scripts\activate
        ```
    - **macOS y Linux**:
        ```sh
        source venv/bin/activate
        ```

4. **Instalar dependencias**:
    ```sh
    pip install -r requirements.txt
    ```

## Cargar Datos en la Base de Datos (SQLite3)

1. **Aplicar migraciones**:
    ```sh
    python manage.py migrate
    ```

2. **Cargar datos desde `data.json`**:
    ```sh
    python manage.py loaddata data.json
    ```

Esto configurará y poblará tu base de datos con los datos iniciales.

## Levantar el Servidor

Para levantar el servidor, usa el siguiente comando:

```sh
py manage.py runserver
```
