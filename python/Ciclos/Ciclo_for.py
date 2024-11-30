"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 29 - 10 -2024
Descripción: Uso de ciclo for
"""

"""
El ciclo for se utiliza para iterar sobre una secuencia (como una lista, tupla o cadena) y ejecutar un bloque de código 
para cada elemento de esa secuencia.

Sintaxis:
    for variable in secuencia:
        -> # Código a ejecutar con el valor de la variable dentro de la secuencia.
    
    Nota: Nuevamente, no hay llaves, sino que se deja un espacio. 
"""

print("\t *** Ejemplo de ciclo for ***")

frase = input("Ingresa una frase: ")

# Tomamos un valor en particular (carácter) de toda la secuencia (frase)
for caracter in frase:
    print(caracter, end = "- ") # El "end =" controla el carácter que se imprime al final de la función print()
print("Fin de cadena")

print("\t *** Ejemplo de ciclo for II ***")

alumnos = ["Albert", "Kevin", "Elton", "Diana", "Eden", "Amelia", "Sergio"]

for alumno in alumnos:
    print("Hola", alumno)
    print(f"Hola {alumno}")
    print()