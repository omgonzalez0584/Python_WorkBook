##Exercise 17 Volumen de un cilindro
import math

#Informacion ingresada por teclado
radio = float(input('Introduzca el radio: '))
altura = float(input('Introduzca la altura: '))

#formula matematica
volumen  = (math.pi * (radio ** 2)) * altura

#imprimiendo informacion por teclado
print('El volumen del cilindro: ' + str(round(volumen,2)))
