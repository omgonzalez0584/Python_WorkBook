#Exercise 31: Sum of the Digits in a Integer

#Creacion de variable
suma = 0
cadena = ''

#Ingresando valores por teclado
digitos = input('Introduzca 4  digitos: ')

#sumando los valores
for i in digitos:
    suma += int(i)
    cadena += i + '+' 

#imprimiendo resultados
print('La suma de ' + cadena[0:-1]+ '=' + str(suma))







