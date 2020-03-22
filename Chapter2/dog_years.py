#Exercise 35:  Dog Year

#ingresando datos por teclado
human_years = int(input('Introduzca su edad: '))

#Estructura if-else para realizar la conversion
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
    #Mensaje si el usuario ingresa un numero negativo o cero
    print('Error! , debe ingresar un numero mayor a cero.')
