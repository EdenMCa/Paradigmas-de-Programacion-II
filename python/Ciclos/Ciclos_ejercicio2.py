"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 24 - 10 -2024
Descripción: Programa que calcula la suma acumulativa de todos los números dentro de un rango establecido.
"""

print("\t *** Programa que calcula la suma acumulativa entre 2 números ***" )

# Solicitamos al usuario que ingrese el número inicial.
num_inicial = int(input("Ingrese el número inicial: "))
# Solicitamos al usuario que ingrese el número final.
num_final = int(input("Ingrese el número final: "))

# Inicializamos el contador en 0, el cual ocuparemos para almacenar la suma de los números.
acumulador = 0
# Iniciamos un ciclo while que se ejecutará mientras num_inicial sea menor o igual a num_final.
while num_inicial <= num_final:
    # Aquí se suma el valor de num_inicial al acumulador.
    acumulador += num_inicial
    # Incrementamos el contador en 1, para avanzar al siguiente número.
    num_inicial += 1
# Imprimimos la suma acumulativa.
print(f"La suma de {num_inicial} hasta {num_final} es: {acumulador}")
