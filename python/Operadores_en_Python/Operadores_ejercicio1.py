"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 18 - 10 - 2024
Descripción:
"""

print("\t BONIFICACIÓN BUEN FIN")

gasto = float(input("¿Qué cantidad gastó? "))
cantidad = gasto > 5000
print()
MSI = (input("¿La compra fue a MSI? "))
MSI = MSI.lower() == "si"
print(MSI)

print(f"Aplica bonificación de Buen Fin: {cantidad or MSI}")


