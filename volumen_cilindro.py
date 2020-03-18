##Exercise 17 Volumen de un cilindro
import math

def volumen_cilindro(radio,altura):
    """Calcular el volumen de un cilindro."""
    volumen  = (math.pi * (radio ** 2)) * altura

    return round(volumen,2)  # retornando el resultado

#Informacion ingresada por teclado
radio = float(input('Introduzca el radio: '))
altura = float(input('Introduzca la altura: '))

#imprimiendo informacion por teclado
print('El volumen del cilindro: ' + str(volumen_cilindro(radio,altura)))
