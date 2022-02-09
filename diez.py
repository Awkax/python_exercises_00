"""
Ejercicio 10. El programa tiene que pedir la nota de 15 alumnos y sacar por pantalla cuántos han aprobado y cuántos han suspendido.
"""
print("----------Ejercicio 10--------------")
contador = 1
aprobados = 0
suspendidos = 0

numero_alumnos = int(input("¿Cuántos alumnos tienes? "))

while contador <= numero_alumnos:
    nota = int(input(f"¿Qué nota tiene el alumno {contador}? "))
    if nota >= 5:
        aprobados += 1
    else:
        suspendidos += 1
    contador += 1

print(f"Han suspendido {suspendidos} alumnos, pero han aprobado {aprobados}!")