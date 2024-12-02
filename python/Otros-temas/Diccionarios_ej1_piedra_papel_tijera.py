"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 15 - 11 -2024
Descripción: Programa en el cual implementamos el clásico juego de Piedra, Papel o Tijera entre un usuario y la CPU.
El resultado de la partida se determina mediante un diccionario.
"""
from random import randint # Importa la función randint para generar números aleatorios

# Diccionario que define qué opción vence a cuál
juego = {"Piedra": "Tijera", "Papel": "Piedra", "Tijera": "Papel"}

# Contadores para las victorias del jugador, la CPU y empates
victorias_jugador = 0
victorias_cpu = 0
empates = 0

# Inicializamos la variable opcion_elegida en -1 para que entre al ciclo al menos una vez
opcion_elegida = -1
while opcion_elegida != 0:
    print()
    print("\t *** Juego de piedra, papel o tijera ***")
    print(f"Victorias del jugador: {victorias_jugador}, Empates: {empates}, Victorias del CPU: {victorias_cpu}")
    print()
    print("----------------------------------")
    print("- [1]. Piedra                    -")
    print("- [2]. Papel                     -")
    print("- [3]. Tijera                    -")
    print("- [0]. Salir                     -")
    print("----------------------------------")
    print()

    # Solicita la opción del jugador
    opcion_elegida = int(input("Seleccione una opción: "))

    # Si el jugador elige una opción válida (1, 2 o 3) entramos en este bloque de código.
    if opcion_elegida == 1 or opcion_elegida == 2 or opcion_elegida == 3:
        # Genera una opción aleatoria para la CPU
        cpu = randint(1, 3)

        # Crea una lista con las opciones para el jugador y la CPU
        opciones = ["Piedra", "Papel", "Tijera"]
        # Traduce las opciones a palabras
        op_jugador = opciones[opcion_elegida - 1]
        op_cpu = opciones[cpu - 1]

        print(f"Jugador: {op_jugador}. CPU: {op_cpu}.")

        # Comparar las elecciones usando el diccionario
        if op_jugador == op_cpu:
            print("El resultado es un empate.")
            empates += 1
        elif juego[op_jugador] == op_cpu:
            print("¡Ganaste!")
            victorias_jugador += 1
        else:
            print("Perdiste.")
            victorias_cpu += 1

    # Si el jugador elige la opción 0, el programa termina
    elif opcion_elegida == 0:
        print("Saliendo del programa... c:")
        break
    else:
        # Si el jugador ingresa una opción no válida, se muestra un mensaje de error
        print("Opción no válida, intente de nuevo.")