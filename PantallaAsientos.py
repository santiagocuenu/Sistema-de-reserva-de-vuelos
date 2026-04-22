class PantallaAsientos:
    def __simbolo(self, num, asientos_disponibles):
        if num in asientos_disponibles:
            return f"🟢{num}"
        else:
            return f"🔴{num}"

    def mostrar_mapa(self, asientos_disponibles):
        print("\n" + "="*25)
        print("    MAPA DEL AVIÓN")
        print("="*25)

        # Premium (1-10)
        print("\n[ PREMIUM ]")
        p = list(range(1, 11))
        print(f"      {self.__simbolo(p[0], asientos_disponibles)} {self.__simbolo(p[1], asientos_disponibles)}")
        print(f"{self.__simbolo(p[2], asientos_disponibles)} {self.__simbolo(p[3], asientos_disponibles)}    {self.__simbolo(p[4], asientos_disponibles)} {self.__simbolo(p[5], asientos_disponibles)}")

        # Normal (11-20)
        print("\n[ NORMAL ]")
        n = list(range(11, 21))
        for i in range(0, len(n), 4):
            fila = n[i:i+4]
            print("  ".join(self.__simbolo(x, asientos_disponibles) for x in fila))

        # Económica (21-35)
        print("\n[ ECONÓMICA ]")
        e = list(range(21, 36))
        for i in range(0, len(e), 5):
            fila = e[i:i+5]
            print(" ".join(self.__simbolo(x, asientos_disponibles) for x in fila))
        
        print("\n" + "="*25 + "\n")


# ==========================================
# FUNCIÓN DE PRUEBA (Fuera de la clase)
# ==========================================
def probar_pantalla_independiente():
    # 1. Instanciamos la pantalla (ya no pide nada entre los paréntesis)
    mi_pantalla = PantallaAsientos()
    
    # 2. Simulamos una lista de asientos libres.
    # Digamos que el avión tiene 35 asientos, pero el 2, el 5, el 15 y el 22 ya se vendieron.
    asientos_vendidos = [2, 5, 15, 22,1]
    asientos_libres = [i for i in range(1, 36) if i not in asientos_vendidos]
    
    # 3. Probamos la pantalla pasándole solo la lista
    print("--- INICIANDO PRUEBA VISUAL ---")
    mi_pantalla.mostrar_mapa(asientos_libres)

# Esto hace que la prueba solo corra si ejecutas este archivo directamente
if __name__ == "__main__":
    probar_pantalla_independiente()

