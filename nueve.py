"""
Ejercicio 9. Hacer un programa que pida numeros al usuario indefinidamente hasta meter el numero 111.
"""

print("-------Ejercicio 9--------")

numero = int(input("Número: "))

while numero != 111:
    numero = int(input("Número: "))
else:
    print("Al fin!")

