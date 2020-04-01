#Exercise 47

from date_to_number import date_to_numbers as dtn

print('Descubra su signo zodiacal.')
mes = input('Introduzca el mes: ')
dia = int(input('Introzca el dia: '))

if dtn(mes,dia) >= dtn('enero',20) and dtn(mes,dia) <= dtn('febrero',18):
    print('Su signo zodical es Acuario')
elif dtn(mes,dia) >= dtn('febrero',19) and dtn(mes,dia) <= dtn('marzo',20):
    print('Su signo zodical es Piscis')
elif dtn(mes,dia) >= dtn('marzo',21) and dtn(mes,dia) <= dtn('abril',19):
    print('Su signo zodical es Aries')
elif dtn(mes,dia) >= dtn('abril',20) and dtn(mes,dia) <= dtn('mayo',20):
    print('Su signo zodical es Tauro')
elif dtn(mes,dia) >= dtn('mayo',21) and dtn(mes,dia) <= dtn('junio',20):
    print('Su signo zodical es Geminis')
elif dtn(mes,dia) >= dtn('junio',21) and dtn(mes,dia) <= dtn('julio',22):
    print('Su signo zodical es Cancer')
elif dtn(mes,dia) >= dtn('julio',23) and dtn(mes,dia) <= dtn('agosto',22):
    print('Su signo zodical es Leo')
elif dtn(mes,dia) >= dtn('agosto',23) and dtn(mes,dia) <= dtn('septiembre',22):
    print('Su signo zodical es Virgo')
elif dtn(mes,dia) >= dtn('septiembre',23) and dtn(mes,dia) <= dtn('octubre',22):
    print('Su signo zodical es Libra')
elif dtn(mes,dia) >= dtn('octubre',23) and dtn(mes,dia) <= dtn('noviembre',21):
    print('Su signo zodical es Escorpio')
elif dtn(mes,dia) >= dtn('noviembre',22) and dtn(mes,dia) <= dtn('diciembre',21):
    print('Su signo zodical es Sagitario')
else:
    print('Capricornio')
