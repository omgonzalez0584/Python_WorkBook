#Exercise 40 Name of triangle

side_a = float(input('Introduzca el lado A: '))
side_b = float(input('Introduzca el lado B: '))
side_c = float(input('Introduzca el lado C: '))

if side_a == side_b and side_a == side_c:
    print('El triangulo es Equilatero.')

elif side_a != side_b and side_a != side_c  and side_b != side_c:
    print('El triangulo es Escaleno.')

else:
    print('El triangulo es Isosceles.')
