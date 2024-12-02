"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 13 - 11 -2024
Descripción: En este programa ocupamos listas y tuplas para trabajar con coordenadas que se le solicitan al usuario.
"""
RED = "\033[31m" # Define el color rojo para el texto.
RESET = "\033[0m"  # Define el color de reinicio para volver al color original.

# Función para mostrar el menú principal del programa.
def menu ():
    print("---------------------------------------------------------------------------------------")
    print(f"-  {RED} Rectas a partir de puntos (coordenadas) en el plano cartesiano{RESET}                    -")
    print("-                                                                                     -")
    print("- [1].- Ver coordenadas almacenadas.                                                  -")
    print("- [2].- Agregar coordenada (x,y).                                                     -")
    print("- [3].- Calcular la pendiente y la ecuación de la recta entre dos coordenadas.        -")
    print("- [4].- Eliminar coordenada (x,y).                                                    -")
    print("- [0].- Salir                                                                         -")
    print("---------------------------------------------------------------------------------------")

# Función para ver las coordenadas almacenadas.
def ver_coordenadas(coordenadas):
    if coordenadas: # Verificamos si hay coordenadas en la lista.
        print("\nListas de coordenadas almacenadas:")
        i = 1  # Inicia el contador en 1
        for coordenada in coordenadas:
            print(f"Coordenada {i}: ({coordenada[0]}, {coordenada[1]})")
            i += 1  # Incrementa el contador
    else:
        print("\nNo hay coordenadas para mostrar.\n")

# Función para agregar una nueva coordenada. Permite al usuario ingresar una nueva coordenada (x, y) y agregarla a la lista.
def agregar_coordenada(coordenadas):
    x = float(input("\nIngrese la coordenada x: ")) # Solicita el valor de x.
    y = float(input("Ingrese la coordenada y: ")) # Solicita el valor de y.
    coordenadas.append((x, y)) # Agrega la coordenada como una tupla a la lista.
    print(f"La coordenada ({x}, {y}) se agregó con éxito!.")


# Función para calcular la pendiente y la ecuación de la recta entre dos puntos.
def calcular_ecuacion_recta(coordenadas):
    if len(coordenadas) < 2: # Verificamos si hay al menos dos coordenadas.
        print("\nNo hay coordenadas para mostrar.\n")
        return

    print("\nSeleccione dos puntos para calcular la recta:")
    ver_coordenadas(coordenadas) # Mostramos las coordenadas disponibles.

    # Solicitamos al usuario los índices de las coordenadas.
    indice1 = int(input("\nIngrese el índice de la primera coordenada: ")) - 1
    indice2 = int(input("Ingrese el índice de la segunda coordenada: ")) - 1

    # Verificamos que los índices sean válidos y que no sean iguales.
    if 0 <= indice1 < len(coordenadas) and 0 <= indice2 < len(coordenadas) and indice1 != indice2:
        x1, y1 = coordenadas[indice1] # Obtiene la primera coordenada.
        x2, y2 = coordenadas[indice2] # Obtiene la segunda coordenada.

        # Calculamos la pendiente
        if x1 == x2:
            print("La pendiente es indefinida (la recta es vertical).")
            print(f"La ecuación de la recta es: x = {x1}")
        else:
            pendiente = (y2 - y1) / (x2 - x1)
            # Ecuación de la recta: y = mx + b
            b = y1 - pendiente * x1
            print(f"La pendiente entre la coordenada {coordenadas[indice1], coordenadas[indice2]} es: {pendiente}")
            print(f"La ecuación de la recta es: y = {pendiente}x + {b}")
    else:
        print("Índices no válidos. Asegúrese de ingresar dos puntos distintos.")

# Función para eliminar una coordenada.
def eliminar_coordenada(coordenadas):
    if coordenadas: # Verifica si hay coordenadas en la lista.
        ver_coordenadas(coordenadas) # Muestra las coordenadas disponibles.
        # Solicitamos al usuario el índice de la coordenada a eliminar.
        indice = int(input("\nIngrese el índice de la coordenada que desea eliminar: ")) - 1
        if 0 <= indice < len(coordenadas): # Verifica si el índice es válido.
            removed_coordenada = coordenadas.pop(indice) # Elimina la coordenada de la lista.
            print(f"La coordenada {removed_coordenada} ha sido eliminada correctamente.")
        else:
            print("Índice no válido.")
    else:
        print("\nNo hay coordenadas para eliminar.\n")

coordenadas = []  # Lista para almacenar las tuplas de coordenadas.

while True:
    menu() # Llamamos a la función del menú
    opcion = int(input("\nSeleccione una opción: ")) # Solicita la opción al usuario

    # Llamamos a la función tomando en cuenta la opción que el usuario elija.
    if opcion == 1:
        ver_coordenadas(coordenadas)
    elif opcion == 2:
        agregar_coordenada(coordenadas)
    elif opcion == 3:
        calcular_ecuacion_recta(coordenadas)
    elif opcion == 4:
        eliminar_coordenada(coordenadas)
    elif opcion == 0:
        print("Saliendo del programa... :D")
        break
    else:
        print("Opción no válida.")