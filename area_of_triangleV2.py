#Exercise 22 Area of a Triangle 2
import math

#Introduciendo lados del triangulo
s1 = float(input('Ingrese la longitud del primer lado: '))
s2 = float(input('Ingrese la longitud del segundo lado: '))
s3 = float(input('Ingrese la longitud del tercer lado: '))

#Aplicando formulas matematicas
s = (s1 + s2 + s3) / 2

#Utilizando exception cuando no se puede sacar raiz cuadrada
try:
    area = math.sqrt( s * ( s - s1 ) * ( s - s2 ) * ( s - s3 ))
except ValueError:
    print('Un lado es mayor a S, no se puede calcular el area: ')
else:
    #Imprimiendo resultados
    print('\nCalculando area del triangulo....')
    print('=' + str(round(area,2)))
