#Exercise 48 Chinese Zodiac

#Ingresando datos por teclado
try:
    year = int(input('Input your year birthday: '))

    #Estructura if/else que valida el signo zodical chino
    if year % 12 == 8:
        print('Dragon')
    elif year % 12 == 9:
        print('Snake')
    elif year % 12 == 10:
        print('Horse')
    elif year % 12 == 11:
        print('Sheep')
    elif year % 12  == 0:
        print('Monkey')
    elif year % 12 == 1:
        print('Rooster')
    elif year % 12 == 2:
        print('Dog')
    elif year % 12 == 3:
        print('Pig')
    elif year % 12 == 4:
        print('Rat')
    elif year % 12 == 5:
        print('Ox')
    elif year % 12 == 6:
        print('tiger')
    elif year % 12 == 7:
        print('Hare')

except ValueError:
    print('Error, You must enter a year!')
