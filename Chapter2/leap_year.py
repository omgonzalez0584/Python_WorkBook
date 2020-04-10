#Exercise 57: It is a leap year?

try:
#Input data for keyboard.
    year = int(input('Input the year: '))

#If/Else statament
    if (year % 4 == 0) and (year % 100 != 0):
        print('It is a leap year!')
    elif(year % 400 == 0):
        print('It is a leap year!')
    else:
        print('Is is not a leap year!')

except ValueError:
    print('Error,you must to input a year.')
