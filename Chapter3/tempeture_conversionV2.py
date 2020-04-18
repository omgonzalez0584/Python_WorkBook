#Exercise 63  Tempeture conversion Table

print("Tabla de conversion de Temperatura de Celsius a Fahrenheit.")
print("\tCelsius "  + "\tFahrenheit   " )
for i in range(0,11):
    c = i * 10
    f = (c * (9/5)) + 32
    print("\t"+str(c)+"\t\t"+str(f))
