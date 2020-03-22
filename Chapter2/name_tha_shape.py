#Exercise 37: Name that shape

shapes = {3:'Triangulo',4:'Cuadrado',5:'Pentagono',
            6:'Hexagono',7:'Heptagono',8:'Octagono',
            9:'Eneagono',10:'Decagono'}

number_sides = int(input('Introduzca el numero de lados: '))

if number_sides >= 3 and number_sides <= 10:
    print('Es un ' + shapes[number_sides])

else:
    print('Debe escribir un numero entre 3 y 10')
