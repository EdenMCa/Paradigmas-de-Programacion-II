"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 10-10-2024
Descripción:
- Este programa registra y muestra los gastos diarios en diferentes categorías.
- Se utilizan variables para almacenar información sobre el día, pasaje, comida y otros gastos.
- También se incluye un booleano para indicar si los gastos fueron mayores a un presupuesto definido.

"""

mi_variable_dia = "lunes" # Almacena el día de la semana
mi_variable_pasaje = 20 # Almacena el gasto en pasaje
mi_variable_comida = 135.5 # Almacena el gasto en comida
mi_variable_otros_gastos = 34.5 # Almacena otros gastos
mi_variable_booleano_presupuesto = True # Indica si los gastos fueron mayores al presupuesto

print("*** Gastos diarios ***")
print("Día:", mi_variable_dia) # Imprime el día
print("Pasaje:", mi_variable_pasaje) # Imprime el gasto en pasaje
print("Comida:", mi_variable_comida) # Imprime el gasto en comida
print("Otros gastos:", mi_variable_otros_gastos) # Imprime otros gastos
print("¿Fue mayor a mi presupuesto?", mi_variable_booleano_presupuesto) # Imprime el estado del presupuesto

# Actualizamos las variables para el siguiente día.
mi_variable_dia = "Martes"
mi_variable_pasaje = 12
mi_variable_comida = 45.5
mi_variable_otros_gastos = 4.5
mi_variable_booleano_presupuesto = False # Indica que los gastos no fueron mayores al presupuesto

print(" ") # Imprime una línea en blanco
print("*** Gastos diarios ***")
print("Día:", mi_variable_dia) # Imprime el día
print("Pasaje:", mi_variable_pasaje) # Imprime el gasto en pasaje
print("Comida:", mi_variable_comida) # Imprime el gasto en comida
print("Otros gastos:", mi_variable_otros_gastos) # Imprime otros gastos
print("¿Fue mayor a mi presupuesto?", mi_variable_booleano_presupuesto)  # Imprime el estado del presupuesto
