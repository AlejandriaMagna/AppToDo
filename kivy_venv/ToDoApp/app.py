from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle
from kivy.metrics import dp 
from kivy.clock import Clock # ¡NUEVA IMPORTACIÓN para la carga retrasada!
from database import get_all_tasks, add_task, update_task_title, update_task_status, delete_task
from tarea import Tarea

class ToDoApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10)) 

        # ------------------- Sección para agregar tarea -------------------
        add_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(40)) 
        self.task_input = TextInput(hint_text='Escribe una nueva tarea...')
        add_button = Button(text='Agregar', size_hint_x=0.3)
        add_button.bind(on_press=self.add_new_task)
        
        add_box.add_widget(self.task_input)
        add_box.add_widget(add_button)
        self.root.add_widget(add_box)

        # ------------------- Sección para mostrar tareas -------------------
        self.tasks_list = BoxLayout(orientation='vertical', spacing=dp(5), size_hint_y=None) 
        self.tasks_list.bind(minimum_height=self.tasks_list.setter('height'))
        
        scroll_view = ScrollView(size_hint=(1, 1))
        scroll_view.add_widget(self.tasks_list)
        self.root.add_widget(scroll_view)

        # Retrasamos la carga inicial. Se llama a 'self.check_list_size' después de un frame.
        Clock.schedule_once(self.check_list_size, 0)
        return self.root

    def check_list_size(self, dt):
        """Verifica que el ancho de la lista esté definido antes de cargar tareas."""
        if self.tasks_list.width > 0:
            self.load_tasks()
        else:
            # Si el ancho aún es 0, lo programamos para que se verifique de nuevo.
            Clock.schedule_once(self.check_list_size, 0)

    def load_tasks(self):
        self.tasks_list.clear_widgets()
        tasks_data = get_all_tasks()
        
        # Ahora garantizamos que list_width tiene un valor real
        list_width = self.tasks_list.width if self.tasks_list.width > 0 else dp(400) 
        
        for task_id, task_title, task_status in tasks_data:
            tarea_obj = Tarea(titulo=task_title, id=task_id, estado=task_status)
            self.create_task_widget(tarea_obj, list_width)
            
    def create_task_widget(self, tarea: Tarea, list_width):
        
        # 1. CREAR la etiqueta de texto y medir su tamaño
        task_label = Label(
            text=tarea.titulo,
            size_hint_x=0.5,
            text_size=(list_width * 0.5, None),
            valign='top',
            color=(0, 0, 0, 1)
        )
        
        # 2. CALCULAR la altura mínima
        min_height = max(dp(60), task_label.texture_size[1] + dp(20))
        
        # 3. Crear el Contenedor (task_widget) con la altura calculada
        task_widget = BoxLayout(
            orientation='horizontal', 
            size_hint_y=None, 
            height=min_height 
        )
        
        # Dibujar el fondo
        with task_widget.canvas.before:
            if tarea.estado == 'completada':
                Color(0.8, 1, 0.8, 1)
            else:
                Color(1, 1, 1, 1) 
            self.rect = Rectangle(size=task_widget.size, pos=task_widget.pos)
        
        task_widget.bind(size=self.update_rect, pos=self.update_rect) 
        
        # Botones
        complete_button = Button(text='✔', size_hint_x=0.1)
        complete_button.bind(on_press=lambda instance: self.toggle_task_status(tarea.id, tarea.estado))
        
        edit_button = Button(text='Editar', size_hint_x=0.2)
        edit_button.bind(on_press=lambda instance: self.show_edit_popup(tarea.id, tarea.titulo))
        
        delete_button = Button(text='Eliminar', size_hint_x=0.2)
        delete_button.bind(on_press=lambda instance: self.delete_a_task(tarea.id))
        
        # 4. AGREGAR la etiqueta (Label)
        task_widget.add_widget(task_label)
        task_widget.add_widget(complete_button)
        task_widget.add_widget(edit_button)
        task_widget.add_widget(delete_button)
        self.tasks_list.add_widget(task_widget)

    def update_rect(self, instance, value):
        instance.canvas.before.children[-1].pos = instance.pos
        instance.canvas.before.children[-1].size = instance.size
        
    def add_new_task(self, instance):
        task_title = self.task_input.text
        if task_title:
            add_task(task_title)
            self.task_input.text = ''
            self.load_tasks()

    def toggle_task_status(self, task_id, current_status):
        new_status = 'completada' if current_status == 'pendiente' else 'pendiente'
        update_task_status(task_id, new_status)
        self.load_tasks()

    def show_edit_popup(self, task_id, current_title):
        box = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10)) 
        new_title_input = TextInput(text=current_title)
        save_button = Button(text='Guardar Cambios')
        
        box.add_widget(Label(text='Editar Tarea'))
        box.add_widget(new_title_input)
        box.add_widget(save_button)
        
        popup = Popup(title='Editar', content=box, size_hint=(0.8, 0.4))
        save_button.bind(on_press=lambda instance: self.edit_task(task_id, new_title_input.text, popup))
        popup.open()

    def edit_task(self, task_id, new_title, popup):
        if new_title:
            update_task_title(task_id, new_title)
            self.load_tasks()
            popup.dismiss()

    def delete_a_task(self, task_id):
        delete_task(task_id)
        self.load_tasks()

if __name__ == '__main__':
    ToDoApp().run()