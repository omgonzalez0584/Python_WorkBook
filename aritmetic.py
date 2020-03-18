#Exercise 10:  Arithmetic

import  math #Modulo Math

#Capturando datos por teclado
a = int(input('Introduzca el valor de a: '))
b = int(input('Introduzca el valor de b: '))

#Realizando operaciones matematica
print('The sum of ' + str(a) + ' and ' + str(b) + ': ' + str(a + b))
print('The difference when ' + str(b) + ' is subtracted from ' + str(a) + ': ' + str(a - b))
print('the product of ' + str(a) + ' and ' + str(b) +  ': ' + str(a * b))
print('The quotient when ' + str(a) + ' is divided by b ' + str(b) + ': ' + str(round((a / b),2)))
print('The remainder when ' + str(a) + ' is divided by ' + str(b) + ': ' + str(a % b))
print('The result of log10 ' + str(a) + str(math.log(a,10)))
print('The result of ' + str(a) + '^' + str(b) + ': ' + str(a ** b))






