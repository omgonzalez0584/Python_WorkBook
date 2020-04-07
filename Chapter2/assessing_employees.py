#Exercise 53 Assessing Employees

rating = float(input("Input the employee's rating: "))

if rating == 0.0:
    print('The performance is Unacceptable.')
    print('The amount is: 0' )
elif rating == 0.4:
    print('The performance is Acceptable.')
    print('The amount is: ' + str(2400  * rating))
elif rating >= 0.6:
    print('The performance is Meritoriuos.')
    print('The amount is: ' + str(2400 * rating))
