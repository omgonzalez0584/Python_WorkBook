#Execise 16 Area and Volume
import math

#ingresando radio por teclado
radius = float(input('Introduzca el radio: '))

#Aplicando formulas matematicas
area = math.pi * (radius ** 2)
volume =  (4.0 / 3.0) * (math.pi * (radius ** 3))

#Imprimiendo resultados en pantalla
print('El area del circulo: ' + str(round(area,3)))
print('El volumen de una esfera: ' + str(round(volume,3)))
