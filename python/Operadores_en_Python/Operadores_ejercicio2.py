"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 20 - 10 - 2024
Descripción: Programa que verifica si una persona pertenece a la comunidad de la UNSIJ, ya sea como estudiante o profesor.
"""
print("\t *** Comunidad UNSIJ ***")
es_estudiante = input("¿Es estudiante de la UNSIJ? ")
# Pregunta al usuario si es estudiante de la UNSIJ y almacena la respuesta
es_estudiante = es_estudiante.lower() == "si"
# Convierte la respuesta a minúsculas y evalúa si es "si", almacenando el resultado como un booleano
es_profesor = input("¿Es profesor de la UNSIJ? ")
# Pregunta al usuario si es profesor de la UNSIJ y almacena la respuesta
es_profesor = es_profesor.lower() == "si"

print(f"Pertenece a la comunidad UNSIJ: {es_estudiante or es_profesor}")
# Se imprime TRUE si una de las dos condiciones es verdadera, esto significa que pertenece a la comunidad ya sea siendo estudiante o profesor