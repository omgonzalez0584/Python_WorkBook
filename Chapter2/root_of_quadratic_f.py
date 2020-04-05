#Exercise 50: Root of a quadratic function
import math

print('Calcule la raiz de una funcion cuadratica')
a = float(input('Introduzca el valor de a: '))
b = float(input('Introduzca el valor de b: '))
c = float(input('Introduzca el valor de c: '))

#Calculando discriminante
discriminante = (b**2) - (4*a*c)

#Calculando raices
if discriminante < 0:
    print('El discriminante es menor a cero, por lo tanto no tiene una raiz real.')
elif discriminante == 0:
    raiz = -b / (2 * a)
    print('La raiz real: ' + str(raiz))
elif discriminante > 0:
    raiz1 = (-b + (math.sqrt(discriminante))) / (2 * a)
    raiz2 = (-b - (math.sqrt(discriminante))) / (2 * a)
    print('La raiz real 1: ' + str(raiz1))
    print('La raiz real 2: ' + str(raiz2))
