# 🚀 Proyecto Final: Aplicación To-Do List (Kivy + SQLite + POO)

Este proyecto desarrolla una aplicación completa de lista de tareas ("To-Do List") que integra una Interfaz Gráfica de Usuario (GUI) moderna con la persistencia de datos y el paradigma de la Programación Orientada a Objetos (POO).

## 🛠️ Tecnologías y Conceptos Clave

| Componente | Tecnología | Propósito |
| :--- | :--- | :--- |
| **Interfaz Gráfica** | **Kivy** (Librería de Python) | Desarrollo de la GUI multiplataforma y reactiva. |
| **Persistencia** | **SQLite3** | Base de datos ligera para almacenar tareas de forma permanente en el archivo `tareas.db`. |
| **Estructura** | **POO** (Clase `Tarea`) | Modelo de datos para manejar el estado (título, ID, estado) de cada tarea de manera eficiente. |
| **Lógica** | **Python** | Lenguaje principal del backend y la lógica de la aplicación. |

---

## 💻 Instrucciones para Ejecutar el Proyecto

El proyecto está diseñado para ejecutarse dentro de un entorno virtual (venv) con Kivy instalado.

1.  **Navegar a la Carpeta del Proyecto:**
    ```bash
    cd kivy_venv/ToDoApp
    ```

2.  **Activar el Entorno Virtual (Si no está activo):**
    ```bash
    source /Users/usuario/Desktop/AppToDo/kivy_venv/bin/activate
    ```

3.  **Ejecutar la Aplicación:**
    ```bash
    python app.py
    ```

---

## 📸 Evidencia de Funcionalidad y Persistencia de Datos

Se demuestra el cumplimiento de los objetivos de persistencia (Guardado/Carga de datos) y el manejo de registros (CRUD) en la base de datos SQLite.

### 1. Estado Inicial (Creación de Tabla Vacía)

Se demuestra que la tabla `tareas` existe y está vacía después de inicializar la aplicación por primera vez, cumpliendo con la función `create_table()`.

**Comando de Consulta:**
```bash
sqlite3 tareas.db
SELECT * FROM tareas;
