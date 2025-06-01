class Prestamo:
    def __init__(self, id_libro, id_usuario, fecha_prestamo, fecha_devolucion=None):
        self.id_libro = id_libro
        self.id_usuario = id_usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def to_dict(self):
        return self.__dict__
