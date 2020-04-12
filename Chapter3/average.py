#Exercise 61: Average

print('Programa calcula el promedio de una lista de valores.')
value = float(input('Introduzca el valor(Presione 0 para salir): '))
if value == 0:
    print('Error, el primer valor no puede ser 0.')
else:
    lista = []
    lista.append(value)
    while True:
        value = float(input('Introduzca el valor(Presione 0 para salir): '))
        if value == 0:
            break
        else:
            lista.append(value)

    suma = 0
    for i in lista:
        suma += i

    promedio = suma / (len(lista))
    print('El promedio es: ' + str(promedio))
