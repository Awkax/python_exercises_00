"""
Ejercicio 5. Hacer un programa que muestre todos los números entre dos números que diga el usuario.
"""
print("--------Ejercicio 5-------")
uno = int (input("Pon el primer número: "))
dos = int (input("Ahora pon el segundo (tiene que ser mayor al primero): "))
numero = 1

if uno < dos:
    for numero in range (uno, dos):
        print(numero)

