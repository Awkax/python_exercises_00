"""
Ejercicio 4. Pedir dos numeros al usuario y hacer todas las operaciones básicas de una calculadora y mostrarlo por pantalla.
"""

primero = int (input('pon el primer numero: '))
segundo = int (input('pon el segundo: '))

suma = primero + segundo
resta = primero - segundo
resta2 = segundo - primero
multi = primero * segundo
division = primero / segundo
resto = primero%segundo
division2 = segundo / primero
resto2 = segundo%primero

print('----------CALCULADORA----------')
print(f'La suma de los números es {suma}')
print(f'La resta de {primero} y {segundo} es {resta}')
print(f'La resta de {segundo} y {primero} es {resta2}')
print(f'La multiplicación de los números es {multi}')
print(f'La división de de {primero} y {segundo} es {division}')
print(f'El resto de la división de {primero} y {segundo} es {resto}')
print(f'La división de {segundo} y {primero} es {division2}')
print(f'El resto de la división de {segundo} y {primero} es {resto2}')


