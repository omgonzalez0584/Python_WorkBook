#Exercise 38 Month Days to a Number Days

#Ingresando mes
month = input('Introduzca el mes: ')
month = month.lower()

#Estructura if/else para validar dias
if (month == 'abril' or month == 'junio' or
    month == 'septiembre' or month == 'noviembre'):

    print(month.title() + ' tiene 30 dias')

elif (month == 'enero' or month == 'marzo'
    or month == 'mayo' or month == 'julio' or month == 'agosto'
    or month == 'octubre' or month == 'diciembre'):

    print(month.title() + ' tiene 31 dias')

elif month == 'febrero':
    print(month.title() + ' tiene 28 o 29 dias')

else: #Utilizado para cualquier otro dato incorrecto
    print('Debe ingresar un mes..!')
