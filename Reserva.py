class Reserva:
    def __init__(self, nombre, apellido, id_usu, destino,id_avion, silla, precio):        
        self.__nombre_pasajero = nombre
        self.__apellido_usuario = apellido
        self.__id_usuario = id_usu
        self.__destino = destino
        self.__id_asiento = silla
        self.__id_avion = id_avion
        self.__precio_base = precio

    def get_precio_base(self):
        return self.__precio_base
    def get_nombre_pasajero(self):
        return self.__nombre_pasajero
    def get_apellido_usuario(self):
        return self.__apellido_usuario
    def get_id_usuario_(self):
        return self.__id_usuario
    def get_destino(self):
        return self.__destino
    def get_id_asiento(self):
        return self.__id_asiento
    def get_id_avion(self):
        return self.__id_avion
    def calcular_precio_final(self):
        return self.__precio_base

    def mostrar_detalles(self):
        return f"Pasajero: {self.__nombre_pasajero} {self.__apellido_usuario}{self.__id_usuario} | Asiento: {self.__id_asiento} | Destino: {self.__destino} | Avión: {self.__id_avion}"

# SUBCLASES

class ReservaEconomica(Reserva):
    def calcular_precio_final(self):
        return self.get_precio_base()
    
    def mostrar_detalles_economica(self):
        print(f"Pasajero: {self.get_nombre_pasajero()} {self.get_apellido_usuario()}tu id es{self.get_id_usuario_()} | Asiento: {self.get_id_asiento()} | Destino: {self.get_destino()} | Avión: {self.get_id_avion()} | Precio Final: ${self.calcular_precio_final()}")
class ReservaNormal(Reserva):
    def calcular_precio_final(self):
        return self.get_precio_base() * 1.15
    def mostrar_detalles_normal(self):
        print(f"Pasajero: {self.get_nombre_pasajero()} {self.get_apellido_usuario()} tu id es {self.get_id_usuario_()} | Asiento: {self.get_id_asiento()} | Destino: {self.get_destino()} | Avión: {self.get_id_avion()} | Precio Final: ${self.calcular_precio_final()}")

class ReservaPremium(Reserva):
    def calcular_precio_final(self):
        return self.get_precio_base() * 1.40
    def mostrar_detalles_premium(self):
        print(f"Pasajero: {self.get_nombre_pasajero()} {self.get_apellido_usuario()} tu id es {self.get_id_usuario_()} | Asiento: {self.get_id_asiento()} | Destino: {self.get_destino()} | Avión: {self.get_id_avion()} | Precio Final: ${self.calcular_precio_final()}")