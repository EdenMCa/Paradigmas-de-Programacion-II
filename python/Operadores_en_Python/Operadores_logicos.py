"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 18 - 10 - 2024
Descripción:
"""

cadena = input("Ingresa SI o NO: ")
cadena = cadena.lower() == "si"
print(f"¿El resultado es SI? {cadena}")

print()
cadena2 = input("Ingresa de nuevo SI o NO: ")
cadena2 = cadena2.lower() == "no"
print(f"¿El resultado es NO? {cadena2}")

print()
print(f"¿El resultado fue TRUE, TRUE? {cadena and cadena2}")
print()
print(f"¿El resultado TRUE, FALSE? {cadena or cadena2}")
print()
print(f"¿El resultado de la primera cadena fue FALSE? {not cadena}")
print()
print(f"¿El resultado de la segunda cadena fue FALSE? {not cadena2}")