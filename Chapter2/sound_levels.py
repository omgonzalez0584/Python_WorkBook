#Exercise 39: Sound levels

#Diccionario que maneja la tabla de niveles de ruido
sound_level = {130:'jackhammer',106:'gaslownmower',70:'alarm clock',40:'quiet room'}

#Manejo excepciones para ingreso de datos erroneos
try:
    #Ingresando datos por teclado
    decibel_level = int(input('Introduzca el nivel de sonido: '))

#Estructura if/else que valida los niveles de ruido
    if  decibel_level in sound_level.keys():
        print('Noise is: ' + sound_level[decibel_level].title())

    elif decibel_level >= 40 and decibel_level <= 70:
        print('Noise is between ' +  sound_level[40].title() +
                ' and ' + sound_level[70].title())

    elif decibel_level > 70 and decibel_level <= 106:
        print('Noise is between ' + sound_level[70].title() +
                ' and ' + sound_level[106].title())

    elif decibel_level > 106 and decibel_level <= 130:
        print('Noise is between ' + sound_level[106].title() +
                ' and ' + sound_level[130].title())

    elif decibel_level > 130:
        print('The value is loudest noise than in the table!')

    else:
        print('The value is quietest noise than in the table!')

#Excepcion que maneja el ingreso de datos incorrectos
except ValueError:
    print('Error!, Debe introducir un numero..!')
