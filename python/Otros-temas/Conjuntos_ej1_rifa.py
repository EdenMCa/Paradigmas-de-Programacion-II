"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 14 - 11 -2024
Descripción: El programa nos sirve para la rifa de una computadora, utilizamos un conjunto (set) para almacenar correos electrónicos de los participantes.
Para seleccionar al ganador, utilizamos la función random.choice() para elegir aleatoriamente un correo del conjunto de participantes.
"""

import random

# Función para mostrar el menú de opciones disponibles.
def menu ():
    print("---------------------------------------------------")
    print("-             RIFA DE UNA COMPUTADORA             -")
    print("-                                                 -")
    print("- [1].- Ver correos de participantes.             -")
    print("- [2].- Agregar correo de participante.           -")
    print("- [3].- Eliminar correo de participante.          -")
    print("- [4].- Seleccionar ganador.                      -")
    print("- [0].- Salir                                     -")
    print("---------------------------------------------------")

# Función para ver los correos de los participantes.
def ver_correos(participantes):
    if participantes: # Verificamos si hay participantes registrados.
        print("\nCorreos de los participantes:")
        i = 1
        for correo in participantes:
            print(f"{i}. {correo}")
            i += 1
    else:
        print("\nNo hay participantes para mostrar.")

# Función para agregar un correo de participante.
def agregar_correo(participantes):
    correo = input("\nIngrese el correo electrónico del participante: ")
    if correo in participantes: # Verificamos si el correo ya está registrado.
        print("El correo ya está registrado. Intente con otro.")
    else:
        participantes.add(correo) # Si el correo no está registrado, lo agregamos al conjunto.
        print(f"El correo {correo} se ha agregado correctamente.")

# Función para eliminar un correo de participante.
def eliminar_correo(participantes):
    if participantes: # Verificamos si hay participantes registrados.
        ver_correos(participantes) # Muestramos los correos registrados.
        correo = input("\nIngrese el correo electrónico que desea eliminar: ") # Solicitamos el correo a eliminar.
        if correo in participantes: # Verificamos si el correo existe en el conjunto.
            participantes.remove(correo)# Eliminamos el correo con remove
            print(f"El correo {correo} se ha eliminado correctamente.")
        else:
            print("El correo no está registrado.")
    else:
        print("\nNo hay participantes registrados para eliminar.")

# Función para seleccionar un ganador.
def seleccionar_ganador(participantes):
    if participantes: # Verificamos si hay participantes registrados.
        lista_participantes = list(participantes) # Convertimos el conjunto en una lista. Esto es para poder usar la
        #función random.choice
        ganador = random.choice(lista_participantes)# Selecciona un ganador de forma aleatoria.
        print(f"\n¡El correo ganador es: {ganador}!")
    else:
        print("\nNo hay participantes registrados para la rifa.")


# Menú principal
participantes = set()  # Conjunto para almacenar los correos de los participantes.

# Inicializamos la variable opcion
opcion = -1
while opcion != 0:
    menu() # Llamamos a la función menú
    opcion = int(input("\nSeleccione una opción: "))

    # Tomando en cuenta la opción elegida por el usuario, llamamos a la función adecuada.
    if opcion == 1:
        ver_correos(participantes) # Llamamos a la función para ver los correos.
    elif opcion == 2:
        agregar_correo(participantes) # Llamamos a la función para agregar un correo.
    elif opcion == 3:
        eliminar_correo(participantes) # Llamamos a la función para eliminar un correo.
    elif opcion == 4:
        seleccionar_ganador(participantes) # Llamamos a la función para seleccionar un ganador.
    elif opcion == 0:
        print("Saliendo del programa... :D")
        break
    else:
        print("Opción no válida.")
