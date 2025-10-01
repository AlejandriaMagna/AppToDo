import sqlite3

# Conectar a la base de datos (se crea si no existe)
def connect_db():
    conn = sqlite3.connect('tareas.db')
    return conn

# Crear la tabla de tareas con el campo 'estado'
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            estado TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Agregar una nueva tarea (con estado inicial 'pendiente')
def add_task(titulo):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tareas (titulo, estado) VALUES (?, ?)', (titulo, 'pendiente'))
    conn.commit()
    conn.close()

# Obtener todas las tareas
def get_all_tasks():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, titulo, estado FROM tareas')
    tasks = cursor.fetchall()
    conn.close()
    return tasks

# Editar el título de una tarea
def update_task_title(task_id, new_title):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE tareas SET titulo = ? WHERE id = ?', (new_title, task_id))
    conn.commit()
    conn.close()

# Cambiar el estado de una tarea
def update_task_status(task_id, new_status):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE tareas SET estado = ? WHERE id = ?', (new_status, task_id))
    conn.commit()
    conn.close()

# Eliminar una tarea
def delete_task(task_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tareas WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

# Inicializar la base de datos al inicio
create_table()