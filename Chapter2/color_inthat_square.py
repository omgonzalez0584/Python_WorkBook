#Exercise 45 Color in that square
import re

#Diccionario que guarda las posiciones iniciales de las columnas.
dict_column = {'a':'black','b':'white','c':'black',
                'd':'white','e':'black','f':'white',
                'g':'black','f':'white'}

#Introduciendo valores por teclado y separando la cadena.
posicion = input('Introduzca la posicion en el tablero de ajedrez: ')
columna = posicion[0]
fila = int(posicion[1:3])

if (fila >= 1 and fila <= 8) and (re.match('[abcdefg]',columna)):
    """Esta estructura valida que el usuario ingrese
        un valor de 1 a 8 y a hasta f"""

#asignando posicion a la columna.
    columna = dict_column[columna]

#Estructura if/else que determina el color del cuadrante.
    if columna == 'white':
        if fila % 2 == 0:
            print('The square is black.')
        else:
            print('The square is white.')

    elif columna == 'black':
        if fila % 2 == 1:
            print('The square is black.')
        else:
            print('The square is white.')

else:
    print('Posicion no esta disponible en el tablero.')
