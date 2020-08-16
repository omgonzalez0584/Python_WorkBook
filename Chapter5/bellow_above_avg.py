#!/usr/bin/env python3

numbers = []
avg ,sum = (0,0)

while True:
    number = input('Input the number: ')
    if number == '':
        break
    else:
        numbers.append(int(number))
        sum += int(number)

avg = sum / len(numbers)
print("The Average is:{:.2f}".format(avg))

above = [i for i in numbers if i > avg]
above.sort()
print("The numbers above the avg: {}".format(above))

below = [i for i in numbers if i < avg]
below.sort()
print("The numbers below the avg: {}".format(below))
