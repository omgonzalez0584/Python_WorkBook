#Exercise 28 Wind Chill

#ingresando datos por teclado
t = float(input('Introduzca la temperatura: '))
v = float(input('Introduzca la velocidad: '))

#Calculando WindChill
if t < 10 and v >= 4.8:
    wci = 13.12 + ( 0.6215 * t ) - ( 11.37 * ( v ** 0.16 ))  + ( 0.3965 * t * (v ** 0.16))
    print('Wind Chill Index: ' + str(round(wci,2)))
else:
    print('Los datos no son validos!')
    print('Temperatura debe ser < 10 y la velocidad >= 4.8')
