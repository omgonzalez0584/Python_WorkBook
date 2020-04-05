#Exercise 51 Letter Grade to Grade Points

print('Programa indica el puntaje de una calificacion.')
letter = input('Introduzca la nota: ')
letter = letter.upper()

if letter == 'A+' or letter == 'A':
    print('Su puntaje es de 4.0')
elif letter == 'A-':
    print('Su puntaje es de 3.7')
elif letter == 'B+':
    print('Su puntaje es de 3.3')
elif letter == 'B':
    print('Su puntaje es de 3.0')
elif letter == 'B-':
    print('Su puntaje es de 2.7')
elif letter == 'C+':
    print('Su puntaje es de 2.3')
elif letter == 'C':
    print('Su puntaje es de 2.0')
elif letter == 'C-':
    print('Su puntaje es de 1.7')
elif letter == 'D+':
    print('Su puntaje es de 1.3')
elif letter == 'D':
    print('Su puntaje es de 1.0')
elif letter == 'F':
    print('Su puntaje es de 0')
else:
    print('Error, favor ingresar una nota correcta, las notas van desde la A hasta F.')
