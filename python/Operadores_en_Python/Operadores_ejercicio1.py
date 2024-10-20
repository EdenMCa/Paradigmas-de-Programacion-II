"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 18 - 10 - 2024
Descripción: Programa que determina si el gasto aplica para una bonificación de buen fin.
"""

print("\t *** BONIFICACIÓN BUEN FIN ***")
gasto = float(input("¿Qué cantidad gastó? "))
# Solicita al usuario la cantidad gastada y la convierte a tipo float para realizar cálculos numéricos
cantidad = gasto > 5000
# Verifica si la cantidad gastada es mayor a 5000 y almacena el resultado.
MSI = (input("¿La compra fue a MSI? "))
# Pregunta al usuario si la compra fue a meses sin intereses (MSI) y almacena la respuesta
MSI = MSI.lower() == "si"
# Convierte la respuesta del usuario a minúsculas y verifica si es "si", almacenando el resultado como un booleano

print(f"Aplica bonificación de Buen Fin: {cantidad and not MSI} ")
# Aplicará la bonificación si la cantidad es mayor a 5000 y no fue a MSI.
# and not se traduce literal como "y no". La expresión and not se utiliza para verificar que una cantidad es mayor a 5000 y que no se pagó a meses sin intereses.
# Si cualquiera de esas condiciones no se cumple, el resultado será False.
