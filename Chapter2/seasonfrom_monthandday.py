#Exercise 46 Season From Month and Day

#Modulo empleado para calcular rango de fechas
from date_to_number import date_to_numbers as dtn

month = input("Introduzca el mes: ")
day = int(input("Introduzca el dia: "))

if dtn(month,day) >= dtn('marzo',20) and dtn(month,day) <= dtn('junio',20):
    print('Spring')
elif dtn(month,day) >= dtn('junio',21) and dtn(month,day) <= dtn('septiembre',21):
    print('Summer')
elif dtn(month,day) >= dtn('septiembre',22) and dtn(month,day) <= dtn('diciembre',20):
    print('Fall')
else:
    print('Winter')
