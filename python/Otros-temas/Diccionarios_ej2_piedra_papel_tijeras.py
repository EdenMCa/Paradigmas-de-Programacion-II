"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 15 - 11 -2024
Descripción: Este programa es el mítico juego de Piedra, Papel, Tijera, Spock, Lagarto de la serie The Big Bang theory.
El usuario elige una opción, y la CPU selecciona aleatoriamente una de las cinco opciones posibles con randint. El programa
utiliza un diccionario para definir las opciones.
"""
from random import randint

# Diccionario de reglas del juego
juego = {"Piedra": ["Tijera", "Lagarto"], "Papel": ["Piedra", "Spock"], "Tijera": ["Papel", "Lagarto"],"Lagarto": ["Papel", "Spock"], "Spock": ["Tijera", "Piedra"] }

# Contadores para las victorias del jugador, la CPU y empates
victorias_jugador = 0
victorias_cpu = 0
empates = 0

# Inicializamos la variable opcion_elegida en -1 para que entre al ciclo al menos una vez
opcion_elegida = -1

# Función para mostrar las reglas del juego
def mostrar_reglas():
    print("\n*** Reglas del Juego: Piedra, Papel, Tijera, Lagarto, Spock ***")
    print("1. Piedra aplasta Tijera y destruye Lagarto.")
    print("2. Papel cubre Piedra y desaprueba Spock.")
    print("3. Tijera corta Papel y decapita Lagarto.")
    print("4. Lagarto come Papel y envenena Spock.")
    print("5. Spock destruye Tijera y vaporiza Piedra.")
    print("6. Si ambos jugadores eligen lo mismo, es un empate.")
    print("7. La cpu va a elegir una de las opciones de manera aleatoria.")


while opcion_elegida != 0:
    print()
    print("\t *** Juego de Piedra, Papel, Tijera, Lagarto, Spock ***")
    # Muestra las estadísticas del jugador
    print(f"Victorías del jugador: {victorias_jugador}, Empates: {empates}, Victorías del CPU: {victorias_cpu}")
    print()

    print("-----------------------------------")
    print("-                                 -")
    print("- [1].- Piedra                    -")
    print("- [2].- Papel                     -")
    print("- [3].- Tijera                    -")
    print("- [4].- Lagarto                   -")
    print("- [5].- Spock                     -")
    print("- [6].- Ver reglas                -")
    print("- [0].- Salir                     -")
    print("-----------------------------------")
    print()

    # Solicita al jugador que seleccione una opción y lo almacenamos como entero.
    opcion_elegida = int(input("Seleccione una opción: "))

    if opcion_elegida == 6:  # Si selecciona esta opción, llamamos a la función mostrar_reglas para mostrar las reglas del juego.
        mostrar_reglas()

    #Si elige una opción entre 1 y 5, entramos a este bloque de código.
    if 1 <= opcion_elegida <= 5:
        cpu = randint(1, 5) # Se genera aleatoriamente un número para la CPU.

        # Lista de opciones para traducir los números a palabras
        opciones = ["Piedra", "Papel", "Tijera", "Lagarto", "Spock"]
        # Obtiene la opción del jugador y de la CPU usando la lista de opciones
        op_jugador = opciones[opcion_elegida - 1]
        op_cpu = opciones[cpu - 1]

        # Si ambos eligen la misma opción, es un empate
        if op_jugador == op_cpu:
            resultado = "empate"
            empates += 1  # Aumenta el contador de empates
        # Si el jugador vence las opciones del CPU (consultamos el diccionario de reglas)
        elif op_cpu in juego[op_jugador]:
            resultado = "victoria"
            victorias_jugador += 1  # Aumenta el contador de victorias del jugador
        else:
            resultado = "derrota"
            victorias_cpu += 1  # Aumenta el contador de victorias de la CPU

        # Muestra el resultado del juego
        print(f"Jugador: {op_jugador}. CPU: {op_cpu}. El resultado es {resultado}.")

    elif opcion_elegida == 0:  # Verifica si el jugador elige salir
        print("Saliendo del programa... c:")
    else:
        print("Opción no válida, intente de nuevo.")
