#Exercise 9: Compound Interest
#Ingresa una cantidad en un cuenta de ahorros y te calcula los intereses por years

amount = float(input('Ingrese la cantidad de dinero en la cuenta: '))

for i in range(1,3+1):
    amount = amount + (amount * 0.04)
    print(str(i)+ ' years: ' + str(round(amount,2)))



