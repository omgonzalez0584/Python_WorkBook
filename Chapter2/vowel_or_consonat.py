#Exercise 36

#ingresando valores por teclado
letter = input('Introduzca la letra: ')
letter = letter.lower()

#Estructura de control que valida
#Si letter es una vocal o consonante
if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print(letter + ' es una vocal')

elif letter == 'y':
    print(letter + ' es aveces una vocal o una consonante')

else:
    print(letter + ' es una consonante')
