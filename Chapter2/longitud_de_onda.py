#Exercise 54: Longitud de onda.

longitud_onda = float(input('Introduzca la longitud de onda: '))


if longitud_onda >= 380 and longitud_onda < 450:
    print('La luz es Violeta.')
elif longitud_onda >= 450  and longitud_onda < 495:
    print('La luz es Azul.')
elif longitud_onda >= 495 and longitud_onda < 570:
    print('La luz es Verde.')
elif longitud_onda >= 570 and longitud_onda < 590:
    print('La luz es Amarilla.')
elif longitud_onda >= 590 and longitud_onda < 620:
    print('La luz es Naranja.')
elif longitud_onda >= 620 and longitud_onda <= 750:
    print('La luz es roja.')
else:
    print('Valores esta fuera de rango, debe ingresar valores entre 380 y 750')
