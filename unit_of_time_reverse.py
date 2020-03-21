#Exercise 25 Units of time reverse

segundos = int(input('Introduzca los segundos: '))

conversion = segundos / 60
ss = segundos % 60
mm = conversion % 60
conversion = conversion / 60
hh = conversion % 24
d = conversion / 24



print(str(d) + ':' + str(hh) + ':' + str(mm) + ':' + str(ss))
