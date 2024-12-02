"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 13 - 11 -2024
Descripción: Este programa calcula el promedio final de un estudiante en base a tres calificaciones parciales y
una calificación de un examen ordinario.
"""

# Definimos la función 'promedio_final' que toma las calificaciones de tres parciales y un examen ordinario como parámetros
def promedio_final(calificacion_1, calificacion_2, calificacion_3, calificacion_ordinario):
    # Calcula el promedio de las tres calificaciones parciales dividiendo la suma entre 3
    promedio_parcial = (calificacion_1 + calificacion_2 + calificacion_3) / 3
    # Calcula el promedio final promediando el promedio parcial con la calificación del examen ordinario
    final = (promedio_parcial + calificacion_ordinario) / 2
    # Retorna los dos promedios como una tupla
    return promedio_parcial, final

# Solicitamos al usuario que ingrese las calificaciones y las convierte a float
calificacion_1 = float(input("Ingrese la primer calificación: "))
calificacion_2 = float(input("Ingrese la segunda calificación: "))
calificacion_3 = float(input("Ingrese la tercera calificación: "))
calificacion_ordinario = float(input("Ingrese la calificación del ordinario: "))
# Llama a la función promedio_final pasando las calificaciones ingresadas y agrega los resultados en
# las variables parcial y final
parcial, final = promedio_final(calificacion_1, calificacion_2, calificacion_3, calificacion_ordinario)

# Imprime el promedio final calculado
print(f"El promedio final es: {final}")
# Imprime el promedio parcial calculado
print(f"El promedio parcial es: {parcial}")