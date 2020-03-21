#Exercise 27 Body mass Index

#Ingresando datos por teclado
print('Programa calcula el indice de masa corporal')
peso = float(input('Introduzca el peso: '))
estatura = float(input('Introduzca la altura: '))
unidades = input('A-Libras - Pulgadas  |  B-Kilogramos - Metros: ')

#Aplicando formula
if unidades.title() == 'A':
    bmi = ( peso / ( estatura * estatura ) ) * 703
    print('Su indice de masa corporal: ' + str(round(bmi,2)))
else:
    bmi = peso / ( estatura * estatura )
    print('Su indice de masa corporal: ' + str(round(bmi,2)))
