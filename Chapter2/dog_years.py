#Exercise 35:  Dog Year
human_years = int(input('Introduzca su edad: '))

if human_years  > 2:
    human_years = human_years - 2
    dog_years = ( human_years * 4 ) + 10.5
    print('Su edad perruna es: ' + str(dog_years))
elif human_years == 2:
    dog_years = 10.5
    print('Su edad perruna es: ' + str(dog_years))

elif human_years == 1:
    dog_years = 10.5 / 2
    print('Su edad perruna es: ' + str(dog_years))

else:
    print('Error! , debe ingresar un numero mayor a cero.')
