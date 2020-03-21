#Exercise 24: Units of time

#Ingresando valores por teclado
dias = int(input('Introduzca los dias: '))
horas = int(input('Introduzca las horas: '))
minutos = int(input('Introduzca los minutos: '))
segundos = int(input('Introduzca los segundos: '))

#Realizando conversiones
days_to_seg = (( dias * 24 ) * 60) * 60 #dias a segundos
hours_to_seg = (horas * 60) * 60  #horas a segundos
min_to_seg = minutos * 60 #Minutoss a segundos

#sumando todos los valores
segundos_totales = days_to_seg + hours_to_seg + min_to_seg + segundos

#Imprimiendo resultado
print('\nEl tiempo en segundos es: ' + str(segundos_totales))
