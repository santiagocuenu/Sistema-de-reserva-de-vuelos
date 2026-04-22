class Usuario:
    def __init__(self, nombre, apellido, id_usu):
        self.__nombre_pasajero = nombre
        self.__apellido_usuario = apellido
        self.__id_usuario = id_usu

    def get_nombre_pasajero(self):
        return self.__nombre_pasajero

    def get_apellido_usuario(self):
        return self.__apellido_usuario

    def get_id_usuario(self):
        return self.__id_usuario