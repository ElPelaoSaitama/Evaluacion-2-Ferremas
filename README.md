# Proyecto Ferremas

## Entorno Virtual (venv)

### ¿Qué es un entorno virtual?

Un entorno virtual en Python es una herramienta que ayuda a mantener dependencias y paquetes aislados para un proyecto específico. Esto es especialmente útil cuando trabajas en múltiples proyectos que pueden tener diferentes versiones de paquetes y bibliotecas. Al usar un entorno virtual, te aseguras de que las dependencias de un proyecto no interfieran con las de otro.

### ¿Por qué usar un entorno virtual?

- **Aislamiento**: Mantiene las dependencias del proyecto separadas de las del sistema global.
- **Control**: Te permite gestionar versiones específicas de paquetes.
- **Reproducibilidad**: Facilita la creación de un entorno de desarrollo consistente para todos los desarrolladores del proyecto.

### Cómo crear un entorno virtual

#### Paso 1: Instalar `virtualenv`

Primero, asegúrate de tener `virtualenv` instalado. Puedes instalarlo usando `pip` (el gestor de paquetes de Python):

```sh
pip install virtualenv

```
### Paso 2 : Crear el entorno virtual

Navega hasta el directorio raíz de tu proyecto y crea un entorno virtual llamado venv (o cualquier otro nombre que prefieras):

```sh
virtualenv venv

```

Esto creará un directorio llamado venv que contiene una instalación aislada de Python y sus paquetes.

### Paso 3 : Activar el entorno virtual

Debes activar el entorno virtual cada vez que empieces a trabajar en tu proyecto. El método para activar el entorno virtual varía según el sistema operativo:

- **Windows**:
```sh
venv\Scripts\activate

```

- **macOS y Linux**:
```sh
source venv/bin/activate

```
Después de activar el entorno virtual, deberías ver el nombre del entorno (por ejemplo, venv) al inicio de tu línea de comando.

### Paso 4 : Instalar dependencias

Con el entorno virtual activado, instala las dependencias necesarias para tu proyecto utilizando el archivo requirements.txt. Esto asegurará que todas las bibliotecas necesarias estén presentes en el entorno virtual:

```sh
pip install -r requirements.txt

```