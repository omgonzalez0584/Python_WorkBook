#Exercise 29: Celsius to Fahrenheit and Kelvin

#Ingresando datos por teclado
celsius = float(input('Introduzca la temperatura en grados Celsius: '))

#Realizando conversiones de temperatura
kelvin = celsius  + 273.15 
fahrenheit = ( celsius * ( 9.0 / 5.0 ) ) + 32 

print('\nGrados Celsius transformado a:  ')
print('Grados Kelvin: ' + str(kelvin))
print('Grados Fahrenheit: ' + str(fahrenheit))



