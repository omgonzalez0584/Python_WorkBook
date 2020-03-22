#Exercise 37: Name that shape

#Diccionario almacena las formas del 3 al 10
shapes = {3:'Triangulo',4:'Cuadrado',5:'Pentagono',
            6:'Hexagono',7:'Heptagono',8:'Octagono',
            9:'Eneagono',10:'Decagono'}

#Estructura Try / Except para validar los datos ingresados
try:
#Ingresando datos por teclado
    number_sides = int(input('Introduzca el numero de lados: '))

#If / Else para validar el rango de numeros
    if number_sides >= 3 and number_sides <= 10:
        print('Es un ' + shapes[number_sides])
    else:
        print('Debe escribir un numero entre 3 y 10')

except ValueError:
    print('Error, debe escribir un numero...')
