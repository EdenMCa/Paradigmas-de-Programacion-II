"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 24 - 10 -2024
Descripción: En este programa utilizamos dos ciclos while para imprimir una serie de números desde el 1 hasta un número ingresado,
en el segundo ejemplo, se imprime solo los números pares que estén dentro del rango..
"""

"""
Sintaxis:
    while condición:
        # Código mientras que la condición sea verdadera.
"""

print("\t * Ejemplo de ciclo while *")

#Se solicita al usuario que ingrese un número y lo guardamos en la variable "num1" convertido en entero.
num1 = int(input("Ingrese un número: "))

# Se indica al usuario que se van a mostrar los números desde 1 hasta el valor ingresado.
print(f"Los números del 1 al {num1} son: ")

# Se inicializa la variable i en 1 para comenzar la cuenta desde ese valor.
i = 1
# Se inicia el ciclo while que se ejecutará mientras i sea menor o igual a num1.
while i <= num1:
    print(i, end = " ")# end = " ": especifica que al final de cada impresión de i, se añade un espacio, en lugar del salto de línea.
    i+= 1 # Incrementa i en 1.
print()# Se imprime un salto de línea.
# Al salir del ciclo, se imprime un mensaje.
print("Fin de la impresión")

print()
print("\t * Ejemplo de ciclo while II *")

# Indicamos que se van a mostrar los números pares desde 0 hasta el valor ingresado.
print(f"Los números pares del 0 al {num1} son:")
# Reiniciamos el valor de la variable.
i = 0
# El ciclo while que se ejecutará mientras i sea menor o igual a num1.
while i <= num1:
    # Imprime el valor actual de i seguido de un espacio.
    print(i, end = " ")
    # Incrementa i en 2 para avanzar al siguiente número par.
    i += 2
print()
# Finalizamos el ciclo con un mensaje.
print("Fin de la impresión")
