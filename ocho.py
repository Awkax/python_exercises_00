"""
Ejercicio 8. ¿Cuánto es el x por ciento de x numero?
"""
print("----------Ejercicio 8----------")


numero = int(input("Número: "))
porcent = int(input("Porcentaje del número: "))
resultado = (porcent*numero)/100

print(f"El {porcent}% de {numero} es {resultado}")