"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 26 - 10 - 2024
Descripción: Este programa verifica que los datos ingresados por el usuario sean iguales a las establecidas.
"""

usuario_correcto = "Eden Mendoza" # Definimos el nombre de usuario correcto.
contrasena_correcta = "Password123" # Definimos la contraseña correcta.

print("\t *** Sistema de autentificación ***")
print()

usuario = input("Ingrese su nombre de usuario: ")# Solicita al usuario que ingrese su nombre de usuario
contrasena = input("Ingresa tu contraseña: ")# Solicita al usuario que ingrese su contraseña

print()
# Compara las respuestas del usuario con las que definimos y muestra el resultado.
# Imprime si el acceso es correcto, evaluando si ambas entradas coinciden.
print(f"¿El acceso es correcto? {usuario == usuario_correcto and contrasena == contrasena_correcta}")