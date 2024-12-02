"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 11 - 11 -2024
Descripción: Este programa gestiona una playlist de videos de YouTube, con ayuda de listas y funciones de estas.
"""

# Códigos para dar color al título.
GREEN = "\033[32m"  # Define el color verde para el texto.
RED = "\033[31m" # Define el color rojo para el texto.
RESET = "\033[0m"  # Define el color de reinicio para volver al color original.

# Definimos la función menu para imprimir las opciones del menú en la consola
def menu ():
    print("-----------------------------------------------------------")
    print("-              PLAYLIST DE VIDEOS DE YOUTUBE              -")
    print("-                                                         -")
    print("- [1].- Ver playlist por videos añadidos.                 -")
    print("- [2].- Ver playlist por orden ascendente (A-Z).          -")
    print("- [3].- Ver playlist por orden descendente (Z-A).         -")
    print("- [4].- Añadir video de YouTube a la playlist.            -")
    print("- [5].- Añadir varios videos de YouTube a la playlist.    -")
    print("- [6].- Eliminar video de la playlist.                    -")
    print("- [0].- Salir                                             -")
    print("-----------------------------------------------------------")

# Lista vacía para almacenar los videos de la playlist
playlist = []  # Define una lista vacía para la playlist.

# Ciclo infinito para mostrar el menú y realizar las acciones según la opción seleccionada por el usuario.
while True:
    menu()  # Llama a la función menu para mostrar las opciones.
    op = int(input("\n¿Qué desea realizar? "))
    i = 1  # Inicia el contador en 1

    # Opción para salir del programa
    if op == 0:
        print(f"\n\t{RED}SALIENDO DEL PROGRAMA... {RESET}")
        break # Termina el bucle y finaliza el programa

    # Opción para ver la playlist por videos añadidos
    elif op == 1:
        if playlist:
            print("PLAYLIST POR VIDEOS AÑADIDOS:")
            for video in playlist:
                print(f"{i}. {video}")  # Imprime el contador y el nombre del video
                i += 1  # Incrementa el contador
            print()  # Salto de línea.
        else:
            print("NO HAY VIDEOS PARA MOSTRAR\n") # Mensaje si la lista está vacía

    # Opción para ver la playlist ordenada de forma ascendente (A-Z)
    elif op == 2:
        i = 1  # Reiniciamos el contador en 1
        if playlist:
            playlist.sort()  # Ordena la lista alfabéticamente.
            print("PLAYLIST POR ORDEN ASCENDENTE (A-Z):")
            for video in playlist: # Itera sobre cada video en la playlist
                print(f"{i}. {video}") # Muestra el índice y el nombre del video
                i += 1
            print()  # Salto de línea.
        else:
            print("NO HAY VIDEOS PARA MOSTRAR\n")

    # Opción para ver la playlist ordenada de forma descendente (Z-A)
    elif op == 3:
        i = 1  # Reinicia el contador en 1
        if playlist:
            playlist.sort(reverse=True)  # Invierte la lista (de Z a A).
            print("PLAYLIST POR ORDEN DESCENDENTE (Z-A):")
            for video in playlist:
                print(f"{i}. {video}")
                i += 1
            print()  # Salto de línea.
        else:
            print("NO HAY VIDEOS PARA MOSTRAR\n")

    # Opción para añadir un solo video a la playlist
    elif op == 4:
        video = input(" Ingresa el nombre del video a agregar a la playlist: ") # Solicitamos al usuario el nombre del video
        playlist.append(video) # Añadimos el video a la lista

        print()  # Salto de línea después de añadir el video.

    # Opción para añadir varios videos a la playlist
    elif op == 5:
        i = 1  # Reinicia el contador en 1
        cantidad = int(input("¿Cuántos videos desea añadir a la playlist? "))
        while i <= cantidad: # Repite el ciclo para añadir los videos
            video = input(f"Ingrese el nombre del video {i}: ") # Solicita el nombre del video
            playlist.append(video) # Añade el video al final de la lista
            i += 1  # Incrementa el contador
        print(f"\nSe añadieron {cantidad} videos a la playlist.\n")
        print()  # Salto de línea después de añadir varios videos.

    # Opción para eliminar un video de la playlist
    elif op == 6:
        if playlist:
            print("PLAYLIST ACTUAL:")
            # Mostrar la lista de videos con índices usando un contador tradicional
            i = 1  # Reiniciar el contador a 1
            for video in playlist:
                print(f"{i}. {video}")
                i += 1  # Incrementar el contador

            # Solicitar al usuario que ingrese el índice del video a eliminar
            indice = int(input("\nIngrese el número del video que desea eliminar: ")) - 1 # Convierte el índice a base 0
            if 0 <= indice < len(playlist): # Verificamos si el índice es válido
                removed_video = playlist.pop(indice)
                print(f"Se eliminó correctamente el video: {removed_video}\n") # Muestra el nombre del video eliminado
            else:
                print(f"{RED}|ERROR| EL ÍNDICE INGRESADO NO ES VÁLIDO{RESET}\n") # Muestra un mensaje de error si el índice no es válido
        else:
            print("NO HAY VIDEOS EN LA PLAYLIST PARA ELIMINAR\n") # Mensaje si la lista está vacía