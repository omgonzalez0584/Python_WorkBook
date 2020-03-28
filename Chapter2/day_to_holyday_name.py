#Exercise 44: Date to holiday name

mes = input('Introduzca el mes: ')
dia = int(input('Introduzca el dia: '))

mes = mes.lower()

if mes == 'enero'  and dia == 1:
    print(" It's new years day !")
elif mes == 'julio'  and dia == 1:
    print(" It's Canada day")
elif mes == 'diciembre'  and dia == 25:
    print(" It's Christmas day")
else:
    print("No tenemos dias feriados para el " + mes + str(dia) )
