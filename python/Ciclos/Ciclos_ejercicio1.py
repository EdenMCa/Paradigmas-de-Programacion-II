"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 24 - 10 -2024
Descripción: Programa que calcula la suma acumulativa de los números desde 0 hasta el número final
proporcionado por el usuario.
"""

print("\t *** Programa que calcula la suma acumulativa ***")
# Solicitamos al usuario un número final para realizar la suma acumulativa
num_final = int(input("Ingrese el número final: "))

# Inicializamos el contador i en 0.
i = 0
# Inicializa el acumulador para almacenar la suma.
acumulador = 0
# Iniciamos un ciclo while que se va a ejecutar hasta que i se igual o menor que num_final.
while i <= num_final:
    # Añade el valor actual de i al acumulador.
    acumulador += i

    # Incrementa i en 1 en cada iteración para avanzar al siguiente número.
    i += 1

# Mostramos el resultado de la suma acumulativa.
print(f"La suma de 0 hasta {num_final} es: {acumulador}")