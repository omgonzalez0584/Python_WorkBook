#Exercise 19: Free Fall

import math

#Ingresando datos por teclado
distance = float(input('Introduzca la distancia: '))

# Calculando velocidad final
final_speed = math.sqrt( (0 **2) + (2* 9.8 * distance))

print('La velocidad final es: ' + str(round(final_speed,2)))
