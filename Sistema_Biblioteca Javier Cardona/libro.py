class Libro:
    def __init__(self, id_libro, titulo, autor, anio, categoria):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.categoria = categoria
        self.disponible = True

    def to_dict(self):
        return self.__dict__
