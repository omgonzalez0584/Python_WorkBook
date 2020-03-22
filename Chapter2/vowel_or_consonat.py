#Exercise 36
import re

#ingresando valores por teclado
letter = input('Introduzca la letra: ')
letter = letter.lower()

#Estructura de control que valida
#Si letter es una vocal o consonante
if re.match('[aeiou]' , letter):
    print(letter + ' es una vocal')

elif letter == 'y':
    print(letter + ' es aveces una vocal o una consonante')

else:
    print(letter + ' es una consonante')
