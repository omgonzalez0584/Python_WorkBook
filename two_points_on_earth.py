#Exercise 12 : Distance Between Two Points on Earth
import math 


#Datos del punto A
t1 = float(input('Introduzca la latitud del punto A: '))
g1 =  float(input('Introduzca la longitud  del punto A: '))

#Datos del punto B
t2 = float(input('Introduzca la latitud del punto B: '))
g2 = float(input('Introduzca la longitud del punto B: '))

#Aplicando formula 
distancia = round(6371.01 * (math.acos((math.sin(math.radians(t1)) * math.sin(math.radians(t2))) +
                        (math.cos(math.radians(t1))  *  math.cos(math.radians(t2))) *
                        (math.cos(math.radians(g1) - math.radians(g2))))),2)

#Imprimiendo resultados
print('La distancia entre los puntos A y B: ' + str(distancia))



