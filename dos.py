"""
Ejercicio 2. Escribir un script que nos muestre por pantalla todos los numeros del 1 al 120
"""

print("-------ejercicio 2-------")

numero = 1
for numero in range (1, 121):
    if numero%2 == 0:
        print(numero)