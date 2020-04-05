#Exercise 50: Root of a quadratic function
import math

#Ingresando datos por teclado
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
    x = -b / (2 * a)
    print('Discriminante es igual a cero, solo tiene una raiz.')
    print('x: ' + str(round(x,4)))
elif discriminante > 0:
    x1 = (-b + (math.sqrt(discriminante))) / (2 * a)
    x2 = (-b - (math.sqrt(discriminante))) / (2 * a)
    print('discriminante es mayor a cero, tiene dos raices reales (x1 , x2).')
    print('x1: ' + str(round(x1,4)))
    print('x2: ' + str(round(x2,4)))
