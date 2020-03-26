#Exercise 43: Faces on Money

#Estructura Try/Except para manejar error introducidos por teclado.
try:
#Introduciendo valores por teclado.
    money = int(input('Introduzca la denominacion del billete: '))

#Estructura if/else para validar los datos.
    if money == 1:
        print('George Washington.')
    elif money == 2:
        print('Thomas Jefferson.')
    elif money == 5:
        print('Abraham Lincoln.')
    elif money == 10:
        print('Alex Hamilton.')
    elif money == 20:
        print('Andrew Jackson.')
    elif money == 50:
        print('Ulysses S. Grant.')
    elif money == 100:
        print('Benjamin Franklin.')

    else:
        print('Esa numeracion no tiene billete.')

except ValueError:
    print('Error, debe introducir valores numericos.')
