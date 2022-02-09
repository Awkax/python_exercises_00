"""
Ejercicio 7. Hacer un programa que muestre todos los numeros impares entre dos numeros que decida el usuario.
"""

print("-------Ejercicio 7--------")

uno = int (input("Pon el primer numero: "))
dos = int (input("pon el segundo (tiene que ser mayor al anterior): "))

if uno < dos:
    for numero in range (uno, (dos + 1)):
       if numero%2 != 0:
            print (numero)