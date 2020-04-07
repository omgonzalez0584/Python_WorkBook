#Exercise 52: Grade Points to Letter Grade.

#Try Except para evitar errores.
try:
#Introduciendo datos por teclado.
    grade_points = float(input('Input your grade points: '))

#Estructura if/else que determina la letra.
    if grade_points >= 0.0 and grade_points < 1.0:
        print('Your letter grade is F')
    elif grade_points >= 1.0 and grade_points < 1.3:
        print('Your letter grade is D')
    elif grade_points >= 1.3 and grade_points < 1.7:
        print('Your letter grade is D+')
    elif grade_points >= 1.7 and grade_points < 2.0:
        print('Your letter grade is C-')
    elif grade_points >= 2.0 and grade_points < 2.3:
        print('Your letter grade is C')
    elif grade_points >= 2.3 and grade_points < 2.7:
        print('Your letter grade is C+')
    elif grade_points >= 2.7 and grade_points < 3.0:
        print('Your letter grade is B-')
    elif grade_points >= 3.0 and grade_points < 3.3:
        print('Your letter grade is B')
    elif grade_points >= 3.3 and grade_points < 3.7:
        print('Your letter grade is B+')
    elif grade_points >= 3.7 and grade_points < 4.0:
        print('Your letter grade is A-')
    elif grade_points >= 4.0 and grade_points < 4.5:
        print('Your letter grade is A')
    elif grade_points >= 4.5 and grade_points <= 5.0:
        print('Your letter is A+')
    else:
        print('El puntaje que ingresaste esta fuera de rango, debes ingresar puntajes de 0 a 5.')

#Exeception que captura el error.
except ValueError:
    print('Error, debe ingresar un numero.')
