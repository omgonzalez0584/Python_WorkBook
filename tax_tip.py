#Exercise 6: Tax and Tip

#Ingresando el costo de la comida
meal = float(input('Introduzca el costo de la comida: '))

#Realizando calculos
tax = meal  * 0.07
tip = meal * 0.18
total = meal + tax + tip

#Imprimiendo el detalle de la factura
print('Detalle de factura')
print('Meal: ' + str(round(meal,2)) + '$')
print('Tax: ' + str(round(tax,2)) + '$')
print('Tip: ' + str(round(tip,2)) + '$')
print('Total: ' + str(round(total,2)) + '$')






