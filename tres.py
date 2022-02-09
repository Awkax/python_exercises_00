"""
Ejercicio 3. Escribir un programa que muestre los cuadrados (un numero multiplicado por si mismo) de los 60 primeros numeros naturales
"""
print('-------ejercicio 3-------')

numero = 1

for numero in range (1, 61):
    resultado = numero*numero
    print(f'El cuadrado de {numero} es {resultado}')