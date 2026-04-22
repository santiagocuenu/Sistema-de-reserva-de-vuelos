class Vuelo:
    def __init__(self, destino, capacidad, num_avion, precio, fecha, asientos_disponibles=None):
        self.__destino = destino
        self.__capacidad_maxima = capacidad
        self.__avion = num_avion
        self.__precio_vuelo = precio
        self.__asientos_disponibles = set(range(1, capacidad + 1))
        self.__fecha = fecha

    def ocupar_asiento(self, ID_asiento):
        if ID_asiento in self.__asientos_disponibles:
            self.__asientos_disponibles.remove(ID_asiento)
            return True
        else:
            return False

    def get_destino(self):
        return self.__destino
    def get_avion(self):
        return self.__avion

    def get_precio_vuelo(self):
        return self.__precio_vuelo

    def get_asientos_disponibles(self):
        return self.__asientos_disponibles
    def mostrar_info_vuelo(self):
        return f"Vuelo {self.__avion} a {self.__destino} | Fecha: {self.__fecha} | Precio: ${self.__precio_vuelo} | Asientos disponibles: {len(self.__asientos_disponibles)}"