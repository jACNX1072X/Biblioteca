class Usuario:
    def __init__(self, id_usuario, nombre, carrera):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.carrera = carrera

    def to_dict(self):
        return self.__dict__
