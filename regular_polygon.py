#Exercise 23 : Area of regular polygon.
import math

#Ingresando longitud y numero de lados.
s = float(input('Introduzca la longitud del poligono: '))
n = int(input('Introduzca el numero de lados: '))

#Aplicando formula
area = ( n * ( s**2 ) ) / ( 4 * math.tan( ( math.pi / n )))

#Imprimiendo resultados por teclado.
print('\nArea de un poligono regular...')
print('= ' + str(round(area,2)))
