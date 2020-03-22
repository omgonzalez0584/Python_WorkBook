#Exercise 36
import re #Modulo de expresiones regulares

#ingresando valores por teclado
letter = input('Introduzca la letra: ')
letter = letter.lower()

#Estructura de control que valida
#Si letter es una vocal o consonante
if re.match('[aeiou]' , letter):
    print(letter.title()  + ' es una vocal')

elif letter == 'y':
    print(letter.title()  + ' es aveces una vocal o una consonante')

elif re.match('[0-9]',letter) or re.match('[!~@#$%^&*()_+]',letter):
    print('Error, debe escribir una letra')

else:
    print(letter.title() + ' es consonante')
