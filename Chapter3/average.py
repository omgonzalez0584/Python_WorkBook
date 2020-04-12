#Exercise 61: Average

#Input data for keyboard
print('Programa calcula el promedio de una lista de valores.')
value = float(input('Introduzca el valor(Presione 0 para salir): '))

#If/Else Statements.
if value == 0:
    print('Error, el primer valor no puede ser 0.')
else:
    suma = value
    contador = 1

#Loop While until that person input 0.
    while True:
        value = float(input('Introduzca el valor(Presione 0 para salir): '))
        if value == 0:
            break
        else:
            suma += value
            contador += 1

#Calculate Average
    promedio = suma / contador
    print('El promedio es: ' + str(promedio))
