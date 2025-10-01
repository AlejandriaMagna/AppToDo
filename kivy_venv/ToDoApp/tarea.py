class Tarea:
    def __init__(self, titulo, id=None, estado="pendiente"):
        self.id = id
        self.titulo = titulo
        self.estado = estado