"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 25 - 11 -2024
Descripción: Este programa genera diferentes pirámides con asteriscos de acuerdo al número ingresado por el usuario,
utilizando funciones.
"""
# Definimos colores para el texto
GREEN = "\033[92m"  # Verde
RESET = "\033[0m"   # Reset de color

# Mostramos un título central "PIRAMIDE" en verde.
print(f"\n\t {GREEN}|PIRAMIDE| {RESET}")
print()

# Solicitamos el número de filas de la pirámide
numero_usuario = int(input("Ingrese un número: "))

# Definimos los caracteres que utilizaremos para construir las pirámides.
asterisco = "*"
espacio = " "

# Función para la pirámide creciente
def piramide_creciente(filas):
    print("\t Ejemplo I: Pirámide creciente")
    for i in range(1, filas + 1): # Ciclo que va de 1 hasta el número de filas ingresado por el usuario
        print(asterisco * i) # Imprime una línea con i asteriscos, aumentando en cada iteración
    print()  # Línea en blanco al final

# Función para la pirámide decreciente
def piramide_decreciente(filas):
    print("\t Ejemplo II: Pirámide decreciente")
    for i in range(filas, 0, -1): # Ciclo que va desde el número de filas hasta 1, decreciendo con cada iteración.
        print(asterisco * i)
    print()  # Línea en blanco al final

# Función para la pirámide centrada
def piramide_centrada(filas):
    print("\t Ejemplo III: Pirámide centrada")
    for i in range(1, filas + 1):  # Ciclo que va de 1 hasta el número de filas ingresado por el usuario
        asteriscos = asterisco * (2 * i - 1)
        espacios = espacio * (filas - i)
        print(espacios + asteriscos)
    print()  # Línea en blanco al final

# Función para la pirámide alineada a la derecha
def piramide_derecha(filas):
    print("\t Ejemplo IV: Pirámide alineada a la derecha")
    for i in range(1, filas + 1): # Ciclo que va de 1 hasta el número de filas ingresado por el usuario
        asteriscos = asterisco * i
        espacios = espacio * (filas - i)
        print(espacios + asteriscos)
    print()  # Línea en blanco al final

# Llamamos a las funciones
piramide_creciente(numero_usuario)
piramide_decreciente(numero_usuario)
piramide_centrada(numero_usuario)
piramide_derecha(numero_usuario)
