#Exercise 15 Distances Unit

#Ingresando valores por teclado
feet = float(input('Introduzca la distancia en pies: '))

#Operaciones de conversion
inches = feet * 12
yards = feet  / 3
miles = yards / 1760

#Imprimiendo resultados
print('El valor en pulgadas: ' + str(round(inches,2)))
print('El valor en yardas: ' + str(round(yards,2)))
print('El valor en millas: ' + str(round(miles,9)))
