"""
Ejercicio 6. Mostrar todas las tabla de multiplicar del 1 al 10. Mostrando el título de la tabla y luego las multiplicaciones.
"""

print("---------Ejercicio 6-----------")

numero = 0

for titulo in range (1, 11):
    print(f"---Tabla del {titulo}---")

    for numero in range (1, 11):
        print(f"{numero} x {titulo} = {numero*titulo}")

    print("\n")