#Exercise 49 Richter Scale

#Ingresando datos por teclado
magnitude = float(input('Input the magnitude: '))

#Estructura que determina la escala de la magnitud
if magnitude <= 2.0:
    print('That magintude ' + str(magnitude) +
            ' is considered to be a Micro Earthquake')

elif magnitude > 2.0 and magnitude <= 3.0:
    print('That magintude ' + str(magnitude) +
            ' is considered to be a very Minor Earthquake')

elif magnitude > 3.0 and magnitude <= 4.0:
    print('That magintude ' + str(magnitude) +
            ' is considered to be a Minor Earthquake')

elif magnitude > 4.0 and magnitude <= 5.0:
    print('That magintude ' + str(magnitude) +
            ' is considered to be a Light Earthquake')

elif magnitude > 5.0 and magnitude <= 6.0:
    print('That magintude ' + str(magnitude) +
            ' is considered to be a Moderate Earthquake')

elif magnitude > 6.0 and magnitude <= 7.0:
    print('That magintude ' + str(magnitude) +
            ' is considered to be a Strong Earthquake')

elif magnitude > 7.0 and magnitude <= 8.0:
    print('That magintude ' + str(magnitude) +
            ' is considered to be a Major Earthquake')

elif magnitude > 8.0 and magnitude <= 10.0:
    print('That magintude ' + str(magnitude) +
            ' is considered to be a Great Earthquake')

else:
    print('That magintude ' + str(magnitude) +
        ' is considered to be a Meteoric Earthquake')
