#Exercise 55 Frequency To Name

#Try/Except para validar que los datos ingresados sean los correctos.
try:

#Ingreando datos por teclado.
    frequency = float(input('Input the Frequency: '))

#Estructura if/else
    if frequency < 3e9:
        print('It is Radio Waves.')
    elif frequency >= 3e9 and frequency < 3e12:
        print('It is Micro Waves.')
    elif frequency >= 3e12 and frequency < 4.3e14:
        print('It is Infrared Light.')
    elif frequency >= 4.3e14 and frequency < 7.5e14:
        print('It is Visible Light.')
    elif frequency >= 7.5e14 and frequency < 3e17:
        print('It is Ultraviolet Light.')
    elif frequency >= 3e17 and frequency < 3e19:
        print('It is X-rays.')
    elif frequency > 3e19:
        print('Gamma rays.')

except ValueError:
    print('Error!, debes ingresar un numero.')
