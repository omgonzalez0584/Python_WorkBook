#Exercise 38 Month Days to a Number Days

month = input('Introduzca el mes: ')
month = month.lower()

if (month == 'abril' or month == 'junio' or
    month == 'septiembre' or month == 'noviembre'):

    print(month + ' tiene 30 dias')

elif (month == 'enero' or month == 'marzo'
    or month == 'mayo' or month == 'julio' or month == 'agosto'
    or month == 'octubre' or month == 'diciembre'):

    print(month + ' tiene 31 dias')

else:
    print(month + ' tiene 28 o 29 dias')
