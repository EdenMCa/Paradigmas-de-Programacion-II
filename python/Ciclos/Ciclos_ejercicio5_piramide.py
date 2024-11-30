"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 07 - 11 -2024
Descripción: Este programa genera diferentes pirámides con asteriscos de acuerdo al número ingresado por el usuario,
el cual es el encargado de especificar cuantas líneas tendrá nuestra pirámide.
"""

# Definimos un color verde para los textos
GREEN = "\033[32m"
# Código para restablecer el color de texto al predeterminado.
RESET = "\033[0m"

# Mostramos un título central "PIRAMIDE" en verde.
print(f"\n\t {GREEN}|PIRAMIDE| {RESET}")
print()

# Solicitamos al usuario que ingrese un número para definir el tamaño de las pirámides.
numero_usuario = int(input("Ingrese un número: "))

# Definimos los caracteres que utilizaremos para construir las pirámides.
asterisco = "*"
espacio = " "

# Ejemplo I: Pirámide creciente
print("\t Ejemplo I")
# Usamos un ciclo for que va desde 1 hasta el número ingresado por el usuario.
for i in range (1,numero_usuario + 1):
    # Generamos una cadena de asteriscos el cual crece con cada iteración.
    asteriscos = asterisco * i
    # Imprimimos la pirámide
    print(asteriscos)

# Ejemplo II: Pirámide decreciente
print("\t Ejemplo II")
# Usamos un ciclo for que comienza en el número ingresado por el usuario y decrece hasta el número 1.
for i in range (numero_usuario, 0, -1):
    # Generamos una cadena de asteriscos cuyo tamaño decrece con cada iteración.
    asteriscos = asterisco * i
    # Imprimimos la pirámide
    print(asteriscos)

# Ejemplo III: Pirámide centrada
print("\t Ejemplo III")
# Usamos un ciclo for que va desde 1 hasta el número ingresado por el usuario.
for i in range (1, numero_usuario + 1):
    # Generamos una cadena de asteriscos, cuyo tamaño corresponde a números impares (2 * i - 1).
    asteriscos = asterisco * (2 * i - 1)
    # El cálculo (numero_usuario - i) determina cuántos espacios en blanco necesita cada fila para alinear los asteriscos al centro.
    espacios = espacio * (numero_usuario - i)
    # Se imprime la línea con los espacios y los asteriscos combinados.
    print(espacios + asteriscos)

# Ejemplo IV: Pirámide alineada a la derecha
print("\t Ejemplo IV")
# Usamos un ciclo for que comienza en el número ingresado por el usuario y decrece hasta el número 1.
for i in range(1,numero_usuario + 1):
    # Generamos una cadena de asteriscos creciente.
    asteriscos = asterisco * i
    # El cálculo (numero_usuario - i) determina cuántos espacios en blanco necesita cada fila.
    espacios = espacio * (numero_usuario - i)
    # Se imprime la pirámide
    print(f"{espacios}{asteriscos}")