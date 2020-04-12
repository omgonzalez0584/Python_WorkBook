#Exercise 61: Average

print('Programa calcula el promedio de una lista de valores.')
value = float(input('Introduzca el valor(Presione 0 para salir): '))
if value == 0:
    print('Error, el primer valor no puede ser 0.')
else:
    suma = value
    contador = 1
    while True:
        value = float(input('Introduzca el valor(Presione 0 para salir): '))
        if value == 0:
            break
        else:
            suma += value
            contador += 1

    promedio = suma / contador
    print('El promedio es: ' + str(promedio))
