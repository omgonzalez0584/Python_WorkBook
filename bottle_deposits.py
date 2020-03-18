#Exercise 5: Bottle Deposits

cantidad_botellas = int(input('Introduzca la cantidad de botellas: '))

#Variables para realizar calculos
total_1 = 0
total_2 = 0
reembolso = 0

#Calcula el total de botellas por tamano
for i in range(cantidad_botellas):
    botellas = float(input("Introduzca el tamano de la botella: "))
    if botellas < 1:
        total_1  = total_1 + 0.10
    else:
        total_2 = total_2 + 0.25

#Calcula el reembolso y lo imprime en pantalla
reembolso =  total_1 + total_2
print('Su reembolso es de: ' + str(round(reembolso,2)) + '$')


