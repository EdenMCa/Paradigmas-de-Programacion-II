"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 18 - 10 - 2024
Descripción: En este programa se solicita al usuario que ingrese "SI" o "NO" y se evalúa las respuestas.
También se utilizan operadores lógicos para determinar el resultado de varias combinaciones de estas respuestas.
"""

cadena = input("Ingresa SI o NO: ")
cadena = cadena.lower() == "si" # Convierte la entrada a minúsculas y verifica si es igual a "sí"
print(f"¿El resultado es SI? {cadena}") # Imprime TRUE si el resultado es verdadero.

print()
cadena2 = input("Ingresa de nuevo SI o NO: ")# Solicita al usuario que ingrese "SI" o "NO" nuevamente
cadena2 = cadena2.lower() == "no" # Convierte la entrada a minúsculas y verifica si es igual a "no"
print(f"¿El resultado es NO? {cadena2}") # Imprime el resultado en booleano.

print()
print(f"¿El resultado fue TRUE, TRUE? {cadena and cadena2}")# Se utiliza el operador AND para verificar si ambas cadenas son verdaderas
print()
print(f"¿En alguno de los casos el resultado TRUE? {cadena or cadena2}")# Utiliza el operador OR para verificar si al menos una de las cadenas fue verdadera
print()
print(f"¿El resultado de la primera cadena fue FALSE? {not cadena}")# Utiliza NOT para verificar si la primera cadena es falsa
print()
print(f"¿El resultado de la segunda cadena fue FALSE? {not cadena2}")# Utiliza NOT para verificar si la segunda cadena es falsa