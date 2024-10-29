"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 27 - 10 - 2024
Descripción: Este programa nos permite realizar el cálculo del promedio de un alumno, tomando en consideración
las calificaciones de los 3 parciales y del ordinario. Con ayuda del if-else creamos condiciones para verificar
si el alumno aprobó o reprobó.
"""

print("\t *** Programa para calcular el promedio de una materia ***")
# Se solicita la calificación del primer parcial y se convierte a un número decimal.
parcial1 = float(input("Ingrese la calificación del parcial 1: "))
# Se solicita la calificación del segundo parcial y se convierte a un número decimal.
parcial2 = float(input("Ingrese la calificación del parcial 2: "))
# Se solicita la calificación del tercer parcial y se convierte a un número decimal.
parcial3 = float(input("Ingrese la calificación del parcial 3: "))
# Se solicita la calificación del examen ordinario y se convierte a un número decimal.
ordinario = float(input("Ingrese la calificación del ordinario: "))

# Se calcula el promedio final tomando en cuenta los parciales y el ordinario.
promedio = ((parcial1 + parcial2 + parcial3) / 3 + ordinario) / 2

print()
# Se verifica si el promedio final es mayor o igual a 6.0
if promedio >= 6.0:
    # Si el promedio es suficiente para aprobar, se muestra el promedio y un mensaje de felicitación.
    print(f"La calificación final es de {promedio:.1f}. ¡Felicidades! Aprobaste.")
# Si la condición no se cumple, quiere decir que el promedio no fue lo suficientemente alto para aprobar.
else:
    print(f"La calificación final es de {promedio:.1f8}. Lo siento, no aprobaste.")