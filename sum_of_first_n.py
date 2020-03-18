#Exercise 7: Sum of the first n Positive Integers

#Ingresando por teclado el valor
n = int(input('Introduzaca el un numero: '))
suma = 0

#Aplicar formula en el rango de 1 a n
for i in range(1,n+1):
    suma = (i * (i + 1)) / 2 
    print('sum = ' + str(suma))
    sum = 0 #Inicializa variable despues de iniciar el calculo


