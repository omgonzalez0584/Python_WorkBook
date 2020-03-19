#Exercise 20:  Ideal Gas Law

#ingresando informacion por teclado.
temperatura = float(input('Introduzca la Temperatura: '))
presion = float(input('Introduzca la presion: '))
volumen = float(input('Introduzca volumen: '))

#Formulas matematicas
temperatura_k = temperatura + 273.15
n = ( presion * volumen ) / ( 8.314 * temperatura_k )

#Imprimiendo resultados
print('\nLos moles de gas: ' + str(round(n,4)))
