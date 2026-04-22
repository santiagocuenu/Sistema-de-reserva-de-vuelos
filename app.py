from Reserva import Reserva, ReservaEconomica, ReservaNormal, ReservaPremium
from PantallaAsientos import PantallaAsientos
from Vuelo import Vuelo
from Usuario import Usuario

import datetime
import random
import tkinter as tk
from tkinter import messagebox
import pickle
import os



""""
def hacer_reserva(vue, usu, res):
    while True:
        print("hola  bienvenido a la aerolínea")
        print("seleccione su destino")
        print("1. Madrid")
        print("2. Paris")
        print("3. Roma")
        print("4. Londres")
        opcion = input("Seleccione su destino: ")
        
        if opcion == "1":
            for i in vue:
                if i.get_destino() == "Madrid":
                    print(i.mostrar_info_vuelo())
        elif opcion == "2":
            for i in vue:
                if i.get_destino() == "Paris":
                    print(i.mostrar_info_vuelo())
        elif opcion == "3":
            for i in vue:
                if i.get_destino() == "Roma":
                    print(i.mostrar_info_vuelo())
        elif opcion == "4":
            for i in vue:
                if i.get_destino() == "Londres":
                    print(i.mostrar_info_vuelo())
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
            
            break
        print("por favor ingrese el codigo de su vuelo a reservar")
        cod_avion = input("Codigo de vuelo: ")
        vuelo_seleccionado = None

        for i in vue:
            if i.get_avion() == cod_avion:
                vuelo_seleccionado = i
                break

        if vuelo_seleccionado is None:
            print("Codigo no encontrado. Por favor, ingrese un codigo válido.")
            continue
        PantallaAsientos().mostrar_mapa(vuelo_seleccionado.get_asientos_disponibles())
        print("ingrese el numero de asiento que desea reservar")
        asiento = int(input("Numero de asiento: "))

        if asiento <= 10 or asiento >= 1:
      
            if i.ocupar_asiento(asiento):
                persona = input("Ingrese solo su nombre: ")
                ape = input("Ingrese solo su apellido: ")
                print("Asiento reservado con éxito.")
                id_usu = random.randint(1000, 9999)
                nuevo_per = Usuario(persona, ape, id_usu)
                usu.append(nuevo_per)
                reserva = ReservaPremium(persona, ape, id_usu, i.get_destino(),cod_avion, asiento, i.get_precio_vuelo())
                res.append(reserva)
                reserva.mostrar_detalles_premium()
                PantallaAsientos().mostrar_mapa(i.get_asientos_disponibles())
                break
            else:
                print("Asiento no disponible. Por favor, elija otro asiento.")
        elif asiento <= 20 or asiento >= 11:
            if i.ocupar_asiento(asiento):
                persona = input("Ingrese solo su nombre: ")
                ape = input("Ingrese solo su apellido: ")
                print("Asiento reservado con éxito.")
                id_usu = random.randint(1000, 9999)
                nuevo_per = Usuario(persona, ape, id_usu)
                usu.append(nuevo_per)
                reserva = ReservaNormal(persona, ape, id_usu, i.get_destino(),cod_avion, asiento, i.get_precio_vuelo())
                res.append(reserva)
                reserva.mostrar_detalles_normal()
            else:
                print("Asiento no disponible. Por favor, elija otro asiento.")
        elif asiento > 20 or asiento <= 35:
            if i.ocupar_asiento(asiento):
                persona = input("Ingrese solo su nombre: ")
                ape = input("Ingrese solo su apellido: ")
                print("Asiento reservado con éxito.")
                id_usu = random.randint(1000, 9999)
                nuevo_per = Usuario(persona, ape, id_usu)
                usu.append(nuevo_per)
                reserva = ReservaEconomica(persona, ape, id_usu, i.get_destino(),cod_avion, asiento, i.get_precio_vuelo())
                res.append(reserva)
                reserva.mostrar_detalles_economica()
            else:
                print("Asiento no disponible. Por favor, elija otro asiento.")
"""
def hacer_reserva(vue, usu, res):

    while True:

        print("\n--- RESERVA DE VUELO ---")
        print("1. Madrid")
        print("2. Paris")
        print("3. Roma")
        print("4. Londres")

        opcion = input("Seleccione destino: ").strip()

        destinos = {
            "1": "Madrid",
            "2": "Paris",
            "3": "Roma",
            "4": "Londres"
        }

        if opcion not in destinos:
            print("⚠ Opción inválida")
            continue

        destino = destinos[opcion]

        # 🔎 MOSTRAR VUELOS
        print("\nVuelos disponibles:")
        for v in vue:
            if v.get_destino() == destino:
                print(v.mostrar_info_vuelo())

        # 🔴 VALIDAR CÓDIGO
        while True:
            cod_avion = input("Código del vuelo (ej: AV123): ").strip().upper()

            if len(cod_avion) >= 4 and cod_avion[:2].isalpha() and cod_avion[2:].isdigit():
                break
            else:
                print("⚠ Código inválido (formato AV123)")

        # 🔎 BUSCAR VUELO
        vuelo = None
        for v in vue:
            if v.get_avion() == cod_avion and v.get_destino() == destino:
                vuelo = v
                break

        if not vuelo:
            print("❌ Vuelo no encontrado")
            continue

        PantallaAsientos().mostrar_mapa(vuelo.get_asientos_disponibles())

        # 🔴 VALIDAR ASIENTO
        while True:
            try:
                asiento = int(input("Número de asiento (1-35): "))
                if 1 <= asiento <= 35:
                    break
                else:
                    print("⚠ Fuera de rango")
            except:
                print("⚠ Debe ingresar un número")

        # 🔴 VALIDAR DISPONIBILIDAD
        if not vuelo.ocupar_asiento(asiento):
            print("❌ Asiento ocupado")
            continue

        # 🔴 VALIDAR NOMBRE
        while True:
            nombre = input("Nombre: ").strip().capitalize()
            if nombre.isalpha():
                break
            print("⚠ Solo letras, sin números")

        while True:
            apellido = input("Apellido: ").strip().capitalize()
            if apellido.isalpha():
                break
            print("⚠ Solo letras, sin números")

        # 👤 CREAR USUARIO
        id_usu = random.randint(1000, 9999)
        usuario = Usuario(nombre, apellido, id_usu)
        usu.append(usuario)

        # 🎟️ CREAR RESERVA
        if 1 <= asiento <= 10:
            reserva = ReservaPremium(nombre, apellido, id_usu, destino, cod_avion, asiento, vuelo.get_precio_vuelo())
        elif 11 <= asiento <= 20:
            reserva = ReservaNormal(nombre, apellido, id_usu, destino, cod_avion, asiento, vuelo.get_precio_vuelo())
        else:
            reserva = ReservaEconomica(nombre, apellido, id_usu, destino, cod_avion, asiento, vuelo.get_precio_vuelo())

        res.append(reserva)

        print("\n✔ Reserva exitosa")
        print(reserva.mostrar_detalles())

        break
"""

def eli_reserva(reser, vuelos):

    print("Ingrese su ID de usuario para revisar sus reservas:")
    id_usuario = int(input("ID de usuario: "))

    reservas_usuario = []

    # 🔍 MOSTRAR RESERVAS DEL USUARIO
    for i in reser:
        if id_usuario == i.get_id_usuario_():
            print(i.mostrar_detalles())
            reservas_usuario.append(i)

    if not reservas_usuario:
        print("No tienes reservas registradas.")
        return

    # 🎯 PEDIR VUELO A ELIMINAR
    print("Ingrese el ID del vuelo para eliminar la reserva:")
    id_vuelo = input("ID de vuelo: ")

    eliminado = eliminar_reserva(reser, vuelos, id_usuario, id_vuelo)

    if eliminado:
        print("Reserva eliminada con éxito")
    else:
        print("No se encontró la reserva")
"""
def eli_reserva(reser, vuelos):

    print("\n--- ELIMINAR RESERVA ---")

    # 🔴 VALIDAR ID
    while True:
        try:
            id_usuario = int(input("Ingrese su ID de usuario: "))
            break
        except:
            print("⚠ Debe ingresar un número válido")

    # 🔎 BUSCAR RESERVAS DEL USUARIO
    reservas_usuario = [r for r in reser if r.get_id_usuario_() == id_usuario]

    if not reservas_usuario:
        print("❌ No tienes reservas registradas")
        return

    # 📄 MOSTRAR RESERVAS
    print("\nTus reservas:")
    for r in reservas_usuario:
        print(r.mostrar_detalles())

    # 🔴 VALIDAR CÓDIGO DE VUELO
    while True:
        id_vuelo = input("Ingrese código del vuelo a eliminar (ej: AV123): ").strip().upper()

        if len(id_vuelo) >= 4 and id_vuelo[:2].isalpha() and id_vuelo[2:].isdigit():
            break
        else:
            print("⚠ Código inválido")

    # 🔎 BUSCAR RESERVA
    reserva_encontrada = None

    for r in reservas_usuario:
        if r.get_id_avion() == id_vuelo:
            reserva_encontrada = r
            break

    if not reserva_encontrada:
        print("❌ No se encontró esa reserva")
        return

    # ⚠ CONFIRMACIÓN
    confirmacion = input("¿Seguro que desea eliminarla? (s/n): ").strip().lower()

    if confirmacion != "s":
        print("Operación cancelada")
        return

    # 🔁 LIBERAR ASIENTO
    for v in vuelos:
        if v.get_avion() == id_vuelo:
            v.get_asientos_disponibles().add(reserva_encontrada.get_id_asiento())
            break

    # ❌ ELIMINAR
    reser.remove(reserva_encontrada)

    print("✔ Reserva eliminada correctamente")
        


def eliminar_reserva(lista_reservas, vuelos, id_usuario, id_vuelo):

    for r in lista_reservas:

        if r.get_id_usuario_() == id_usuario and r.get_id_avion() == id_vuelo:

            # 🔁 DEVOLVER ASIENTO AL AVIÓN
            for v in vuelos:
                if v.get_avion() == id_vuelo:
                    v.get_asientos_disponibles().add(r.get_id_asiento())
                    break

            # ❌ ELIMINAR RESERVA
            lista_reservas.remove(r)

            return True

    return False
"""
def conocer_codigo(usu):
            print("Ingrese su nombre para conocer su código de usuario:")
            nombre_usuario = input("Nombre: ")
            for i in usu:
                if nombre_usuario == i.get_nombre_pasajero():
                    print(f"Su código de usuario es: {i.get_id_usuario()} y el codigo de su vuelo es: {i.get_id_vuelo()}")
                    break
            else:
                print("Usuario no encontrado. Por favor, ingrese un nombre válido.")
"""
def conocer_codigo(usuarios, reservas):

    print("\n--- CONSULTAR CÓDIGO ---")

    # 🔴 VALIDAR NOMBRE
    while True:
        nombre = input("Ingrese su nombre: ").strip().capitalize()

        if nombre.isalpha():
            break
        else:
            print("⚠ Nombre inválido (solo letras, sin espacios extras)")

    # 🔎 BUSCAR USUARIO
    usuario_encontrado = None

    for u in usuarios:
        if u.get_nombre_pasajero() == nombre:
            usuario_encontrado = u
            break

    if not usuario_encontrado:
        print("❌ Usuario no encontrado")
        return

    id_usuario = usuario_encontrado.get_id_usuario()

    print(f"\n✔ Tu ID de usuario es: {id_usuario}")

    # 🔎 BUSCAR SUS RESERVAS
    reservas_usuario = [r for r in reservas if r.get_id_usuario_() == id_usuario]

    if not reservas_usuario:
        print("No tienes reservas registradas")
        return

    print("\nTus vuelos:")
    for r in reservas_usuario:
        print(f"- Vuelo: {r.get_id_avion()} | Asiento: {r.get_id_asiento()}")

"""

def conocer_reservas(reser):
    print("Ingrese su ID de usuario para conocer sus reservas:")
    id_usuario = int(input("ID de usuario: "))

    reservas_usuario = []

    for i in reser:
        if id_usuario == i.get_id_usuario_():
            print(i.mostrar_detalles())
            reservas_usuario.append(i)

    if not reservas_usuario:
        print("No tienes reservas registradas.")
    else:
        print(f"Tienes {len(reservas_usuario)} reserva(s) registradas.")
"""
def conocer_reservas(reser):

    print("\n--- MIS RESERVAS ---")

    # 🔴 VALIDAR ID
    while True:
        try:
            id_usuario = int(input("Ingrese su ID de usuario: ").strip())
            break
        except:
            print("⚠ Debe ingresar un número válido")

    # 🔎 FILTRAR RESERVAS
    reservas_usuario = [r for r in reser if r.get_id_usuario_() == id_usuario]

    if not reservas_usuario:
        print("❌ No tienes reservas registradas")
        return

    # 📄 MOSTRAR RESERVAS
    print(f"\n✔ Tienes {len(reservas_usuario)} reserva(s):\n")

    for idx, r in enumerate(reservas_usuario, 1):
        print(f"{idx}. {r.mostrar_detalles()}")

def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except:
            print("⚠ Ingrese un número válido")

def pedir_opcion(mensaje, opciones):
    while True:
        op = input(mensaje)
        if op in opciones:
            return op
        print("⚠ Opción inválida")

def pedir_asiento():
    while True:
        a = pedir_entero("Número de asiento nuevo (1-35): ")
        if 1 <= a <= 35:
            return a
        print("⚠ Asiento fuera de rango")

def buscar_vuelo(vuelos, codigo):
    for v in vuelos:
        if v.get_avion() == codigo:
            return v
    return None
"""
def cambiar_asiento(reservas, vuelos):

    id_usuario = pedir_entero("ID usuario: ")

    for r in reservas:
        if r.get_id_usuario_() == id_usuario:
            print(r.mostrar_detalles())

            nuevo = pedir_asiento()

            vuelo = buscar_vuelo(vuelos, r.get_id_avion())

            if not vuelo.ocupar_asiento(nuevo):
                print("❌ Asiento ocupado")
                return

            vuelo.get_asientos_disponibles().add(r.get_id_asiento())

            r._Reserva__id_asiento = nuevo

            print("✔ Asiento cambiado")
            return

    print("No encontrado")
"""
def cambiar_asiento(reservas, vuelos):

    print("\n--- CAMBIO DE ASIENTO ---")

    # 🔴 VALIDAR ID
    while True:
        try:
            id_usuario = int(input("Ingrese su ID de usuario: "))
            break
        except:
            print("⚠ Debe ingresar un número válido")

    # 🔎 BUSCAR RESERVAS DEL USUARIO
    reservas_usuario = [r for r in reservas if r.get_id_usuario_() == id_usuario]

    if not reservas_usuario:
        print("❌ No tienes reservas")
        return

    # 📄 MOSTRAR RESERVAS
    print("\nTus reservas:")
    for idx, r in enumerate(reservas_usuario, 1):
        print(f"{idx}. {r.mostrar_detalles()}")

    # 🔴 SELECCIONAR RESERVA
    while True:
        try:
            seleccion = int(input("Seleccione la reserva a cambiar: "))
            if 1 <= seleccion <= len(reservas_usuario):
                reserva = reservas_usuario[seleccion - 1]
                break
            else:
                print("⚠ Opción fuera de rango")
        except:
            print("⚠ Debe ingresar un número válido")

    # 🔎 BUSCAR VUELO
    vuelo = None
    for v in vuelos:
        if v.get_avion() == reserva.get_id_avion():
            vuelo = v
            break

    if not vuelo:
        print("❌ Error interno: vuelo no encontrado")
        return

    PantallaAsientos().mostrar_mapa(vuelo.get_asientos_disponibles())

    # 🔴 VALIDAR NUEVO ASIENTO
    while True:
        try:
            nuevo = int(input("Nuevo asiento (1-35): "))
            if 1 <= nuevo <= 35:
                break
            else:
                print("⚠ Fuera de rango")
        except:
            print("⚠ Debe ingresar un número")

    # 🔴 VALIDAR DISPONIBILIDAD
    if not vuelo.ocupar_asiento(nuevo):
        print("❌ Asiento ocupado")
        return

    # 🔁 LIBERAR ASIENTO ANTERIOR
    vuelo.get_asientos_disponibles().add(reserva.get_id_asiento())

    # 🔄 ACTUALIZAR RESERVA
    reserva._Reserva__id_asiento = nuevo

    print("✔ Asiento cambiado correctamente")

def ver_vuelos_disponibles(vuelos):

    print("\n--- VUELOS DISPONIBLES ---")

    destinos = {
        "1": "Madrid",
        "2": "Paris",
        "3": "Roma",
        "4": "Londres"
    }

    # 🔴 VALIDAR OPCIÓN
    while True:
        print("\nSeleccione destino:")
        for k, v in destinos.items():
            print(f"{k}. {v}")

        opcion = input("Opción: ").strip()

        if opcion in destinos:
            destino = destinos[opcion]
            break
        else:
            print("⚠ Opción inválida")

    # 🔎 FILTRAR VUELOS
    vuelos_filtrados = [v for v in vuelos if v.get_destino() == destino]

    if not vuelos_filtrados:
        print("❌ No hay vuelos disponibles")
        return

    # 📄 MOSTRAR VUELOS
    print(f"\nVuelos hacia {destino}:\n")

    for idx, v in enumerate(vuelos_filtrados, 1):

        total = 35
        disponibles = len(v.get_asientos_disponibles())
        ocupados = total - disponibles

        print(f"{idx}. {v.mostrar_info_vuelo()}")
        print(f"   Asientos disponibles: {disponibles} | Ocupados: {ocupados}\n")

def crear_menu(vuelos, usuarios, reservas):

    ventana = tk.Tk()
    ventana.title("Sistema de Aerolínea ✈️")
    ventana.geometry("400x400")

    def reservar():

        ventana_reserva = tk.Toplevel()
        ventana_reserva.title("Hacer Reserva")

        # DESTINO
        tk.Label(ventana_reserva, text="Destino").pack()
        destino_entry = tk.Entry(ventana_reserva)
        destino_entry.pack()

        # CODIGO
        tk.Label(ventana_reserva, text="Código de vuelo").pack()
        codigo_entry = tk.Entry(ventana_reserva)
        codigo_entry.pack()

        # ASIENTO
        tk.Label(ventana_reserva, text="Asiento (1-35)").pack()
        asiento_entry = tk.Entry(ventana_reserva)
        asiento_entry.pack()

        # NOMBRE
        tk.Label(ventana_reserva, text="Nombre").pack()
        nombre_entry = tk.Entry(ventana_reserva)
        nombre_entry.pack()

        # APELLIDO
        tk.Label(ventana_reserva, text="Apellido").pack()
        apellido_entry = tk.Entry(ventana_reserva)
        apellido_entry.pack()
        def confirmar():

            destino = destino_entry.get()
            codigo = codigo_entry.get()
            nombre = nombre_entry.get()
            apellido = apellido_entry.get()

            # VALIDAR ASIENTO
            try:
                asiento = int(asiento_entry.get())
                if not (1 <= asiento <= 35):
                    raise ValueError
            except:
                messagebox.showerror("Error", "Asiento inválido")
                return

            # BUSCAR VUELO
            vuelo = None
            for v in vuelos:
                if v.get_avion() == codigo and v.get_destino() == destino:
                    vuelo = v
                    break

            if not vuelo:
                messagebox.showerror("Error", "Vuelo no encontrado")
                return

            # OCUPAR ASIENTO
            if not vuelo.ocupar_asiento(asiento):
                messagebox.showerror("Error", "Asiento ocupado")
                return

            # CREAR USUARIO
            id_usu = random.randint(1000, 9999)
            usuario = Usuario(nombre, apellido, id_usu)
            usuarios.append(usuario)

            # CREAR RESERVA
            if 1 <= asiento <= 10:
                reserva = ReservaPremium(nombre, apellido, id_usu, destino, codigo, asiento, vuelo.get_precio_vuelo())
            elif 11 <= asiento <= 20:
                reserva = ReservaNormal(nombre, apellido, id_usu, destino, codigo, asiento, vuelo.get_precio_vuelo())
            else:
                reserva = ReservaEconomica(nombre, apellido, id_usu, destino, codigo, asiento, vuelo.get_precio_vuelo())

            reservas.append(reserva)

            messagebox.showinfo("Éxito", f"Reserva creada\nID usuario: {id_usu}")

            ventana_reserva.destroy()
        tk.Button(ventana_reserva, text="Confirmar", command=confirmar).pack(pady=10)

    def ver_reservas():
        texto = ""
        for r in reservas:
            texto += r.mostrar_detalles() + "\n"
        
        if texto == "":
            texto = "No hay reservas"
        
        messagebox.showinfo("Reservas", texto)

    def eliminar():
        messagebox.showinfo("Info", "Abrir eliminación")

    def cambiar():
        messagebox.showinfo("Info", "Abrir cambio de asiento")

    def stats():
        texto = ""
        for v in vuelos:
            total = 35
            libres = len(v.get_asientos_disponibles())
            ocupados = total - libres
            texto += f"{v.get_avion()} → {ocupados}/{total}\n"

        messagebox.showinfo("Estadísticas", texto)

    def salir():
        ventana.destroy()

    tk.Label(ventana, text="Sistema Aerolínea", font=("Arial", 16)).pack(pady=20)

    tk.Button(ventana, text="Reservar", width=20, command=reservar).pack(pady=5)
    tk.Button(ventana, text="Ver Reservas", width=20, command=ver_reservas).pack(pady=5)
    tk.Button(ventana, text="Eliminar Reserva", width=20, command=eliminar).pack(pady=5)
    tk.Button(ventana, text="Cambiar Asiento", width=20, command=cambiar).pack(pady=5)
    tk.Button(ventana, text="Estadísticas", width=20, command=stats).pack(pady=5)
    tk.Button(ventana, text="Salir", width=20, command=salir).pack(pady=20)

    ventana.mainloop()



def guardar_datos(vuelos, usuarios, reservas):

    with open("datos_aerolinea.pkl", "wb") as archivo:
        pickle.dump((vuelos, usuarios, reservas), archivo)

def cargar_datos():

    if os.path.exists("datos_aerolinea.pkl"):

        with open("datos_aerolinea.pkl", "rb") as archivo:
            vuelos, usuarios, reservas = pickle.load(archivo)

        print("✔ Datos cargados correctamente")
        return vuelos, usuarios, reservas

    return None








def main():

    datos = cargar_datos()

    if datos:
        vuelos_disponibles, usuarios_registrados, reservas_realizadas = datos

    else:
        print("⚡ Primera ejecución: creando datos iniciales...")

        vuelos_disponibles = []
        usuarios_registrados = [] 
        reservas_realizadas = []

    #vuelos madrid disponibles
        vuelo1 = Vuelo("Madrid", 35, "AV123", 500, datetime.date(2026, 4, 1))
        vuelo11 = Vuelo("Madrid", 35, "AV124", 500, datetime.date(2026, 4, 3))
        vuelo12 = Vuelo("Madrid", 35, "AV125", 500, datetime.date(2026, 4, 5))
        vuelos_disponibles.append(vuelo1)
        vuelos_disponibles.append(vuelo11)
        vuelos_disponibles.append(vuelo12)
        # CREAR VUELO
        

        # SIMULAR RESERVAS
        vuelo1.ocupar_asiento(3)
        vuelo1.ocupar_asiento(7)
        vuelo1.ocupar_asiento(15)
    #vuelos paris disponibles
        vuelo2 = Vuelo("Paris", 35, "AV456", 450, datetime.date(2026, 4, 5))
        vuelo21 = Vuelo("Paris", 35, "AV457", 450, datetime.date(2026, 4, 6))
        vuelo22 = Vuelo("Paris", 35, "AV458", 450, datetime.date(2026, 4, 8))
        vuelos_disponibles.append(vuelo2)
        vuelos_disponibles.append(vuelo21)
        vuelos_disponibles.append(vuelo22)

        #vuelos roma disponibles
        vuelo3 = Vuelo("Roma", 35, "AV789", 400, datetime.date(2026, 4, 2))
        vuelo31 = Vuelo("Roma", 35, "AV790", 400, datetime.date(2026, 4, 4))
        vuelo32 = Vuelo("Roma", 35, "AV791", 400, datetime.date(2026, 4, 6))
        vuelos_disponibles.append(vuelo3)
        vuelos_disponibles.append(vuelo31)
        vuelos_disponibles.append(vuelo32)

        #vuelos londres disponibles
        vuelo4 = Vuelo("Londres", 35, "AV321", 550, datetime.date(2026, 4, 7))
        vuelo41 = Vuelo("Londres", 35, "AV322", 550, datetime.date(2026, 4, 9))
        vuelo42 = Vuelo("Londres", 35, "AV323", 550, datetime.date(2026, 4, 11))
        vuelos_disponibles.append(vuelo4)
        vuelos_disponibles.append(vuelo41)
        vuelos_disponibles.append(vuelo42)
            # ==========================
        # 🔥 USUARIOS SIMULADOS
        # ==========================
        u1 = Usuario("Juan", "Perez", 1111)
        u2 = Usuario("Ana", "Lopez", 2222)

        usuarios_registrados.extend([u1, u2])

        # ==========================
        # 🔥 RESERVAS SIMULADAS
        # ==========================

        # Madrid
        vuelo1.ocupar_asiento(5)
        r1 = ReservaPremium("Juan", "Perez", 1111, "Madrid", "AV123", 5, vuelo1.get_precio_vuelo())

        vuelo1.ocupar_asiento(6)
        r2 = ReservaNormal("Ana", "Lopez", 2222, "Madrid", "AV123", 6, vuelo1.get_precio_vuelo())

        # París
        vuelo2.ocupar_asiento(3)
        r3 = ReservaEconomica("Juan", "Perez", 1111, "Paris", "AV456", 3, vuelo2.get_precio_vuelo())

        reservas_realizadas.extend([r1, r2, r3])

    modo = input("1. Consola / 2. Gráfico: ")

    if modo == "1":
                crear_menu(vuelos_disponibles, usuarios_registrados, reservas_realizadas)
    else:
        
        while True:

                print("\n======= AEROLÍNEA =======")
                print("1. Hacer una reserva")
                print("2. Conocer mi código")
                print("3. Eliminar una reserva")
                print("4. Conocer mis reservas")
                print("5. Ver vuelos disponibles")
                print("6. Cambiar asiento")
                print("7. Salir")

                opcion = input("Seleccione una opción: ").strip()

                # 🔴 VALIDACIÓN DE OPCIÓN
                if opcion not in ["1","2","3","4","5","6","7"]:
                    print("⚠ Opción inválida")
                    continue

                # ==========================
                # FUNCIONES
                # ==========================

                if opcion == "1":
                    hacer_reserva(vuelos_disponibles, usuarios_registrados, reservas_realizadas)

                elif opcion == "2":
                    conocer_codigo(usuarios_registrados, reservas_realizadas)

                elif opcion == "3":
                    eli_reserva(reservas_realizadas, vuelos_disponibles)

                elif opcion == "4":
                    conocer_reservas(reservas_realizadas)

                elif opcion == "5":
                    ver_vuelos_disponibles(vuelos_disponibles)

                elif opcion == "6":
                    cambiar_asiento(reservas_realizadas, vuelos_disponibles)

                elif opcion == "7":
                    guardar_datos(vuelos_disponibles, usuarios_registrados, reservas_realizadas)
                    print("\n✔ Datos guardados correctamente")
                    print("✔ Gracias por usar la aerolínea. ¡Hasta luego!")
                    break


if __name__ == "__main__":    
    main()