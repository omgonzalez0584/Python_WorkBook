#Exercise 8: Widgets and Gizmos

#Ingresando datos por teclado
widgets = int(input('Introduzca la cantidad de Widgets: '))
gizmos = int(input('Introduzca la cantidad de Gizmos: '))

#Calculando peso total
weight_widgets = widgets * 75 
weigth_gizmos = gizmos * 112
total_weight = weight_widgets + weigth_gizmos 

#imprimiendo resultado
print('Peso total de Widgets: ' + str(weight_widgets))
print('Peso total de Gizmos: ' + str(weigth_gizmos))
print("El peso total de la orden es: " + str(total_weight) + ' grams')




