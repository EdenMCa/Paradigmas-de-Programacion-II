"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 29 - 10 -2024
Descripción: Este programa simula el juego de piedra, papel o tijera, en donde jugamos contra las opciones aleatorias del CPU.
"""
# Importa la función randint del módulo random para generar números aleatorios
from random import randint

# Inicializa la variable que almacenará la opción elegida por el jugador
opcion_elegida = -1
# Contadores para las victorias del jugador, victorias de la CPU y empates
victorias_jugador = 0
victorias_cpu = 0
empates = 0

# Inicia un bucle que se repetirá mientras el usuario no decida salir
while opcion_elegida != 0:
      print()
      print("\t *** Juego de piedra, papel o tijera ***")
      # Muestra las estadísticas del jugador
      print(f"Victorías del jugador: {victorias_jugador}, empates: {empates}, victorías del CPU: {victorias_cpu}")
      print()

      print("-----------------------------------")
      print("-                                 -")
      print("- [1].- Piedra                    -")
      print("- [2].- Papel                     -")
      print("- [3].- Tijera                    -")
      print("- [0].- Salir                     -")
      print("-----------------------------------")
      print()
      print()
      # Solicita al jugador que seleccione una opción y lo almacenamos como entero.
      opcion_elegida = int(input("Seleccione una opción: "))

      # Verifica que la opción elegida sea válida (1, 2 o 3)
      if opcion_elegida == 1 or opcion_elegida == 2 or opcion_elegida == 3:
            # Genera una opción aleatoria para la CPU (1 para piedra, 2 para papel, 3 para tijera)
            cpu = randint(1, 3)

            # Lista de opciones para traducir los números a palabras
            opciones = ["Piedra", "Papel", "Tijera"]
            # Obtiene la opción del jugador y de la CPU usando la lista de opciones
            op_jugador = opciones[opcion_elegida - 1]
            op_cpu = opciones[cpu - 1]

            # Si ambos eligen la misma opción, es un empate
            if opcion_elegida == cpu:
                  resultado = "empate"
                  empates += 1 # Aumenta el contador de empates
            # Si el jugador vence las opciones del cpu
            elif (opcion_elegida == 1 and cpu == 3) or (opcion_elegida == 2 and cpu == 1) or (
                    opcion_elegida == 3 and cpu == 2):
                  resultado = "victoria" # El jugador gana
                  victorias_jugador += 1 # Aumenta el contador de victorias del jugador
            else:
                  resultado = "derrota" # La CPU gana
                  victorias_cpu += 1 # Aumenta el contador de victorias de la CPU

            # Muestra el resultado del juego
            print(f"Jugador: {op_jugador}. CPU: {op_cpu}. El resultado es {resultado}.")
      elif opcion_elegida == 0: # Verifica si el jugador elige salir
            print("Saliendo del programa... c:")
      else:
            print("Opción no válida, intente de nuevo.")