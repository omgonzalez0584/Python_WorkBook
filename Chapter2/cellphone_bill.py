#Exercise 56:  Cellphone bill.

#Input data for keyboard.
print('The programa calculate a Cellphone Bill.')
minutes = float(input('Input the amount of minutes: '))
text_messages = float(input('Input the amount of text-messages: '))

#If/else Statament for calculate the bill.
if minutes > 50 and text_messages > 50:
    """Calculos si minutos y mensajes son mayores a 50 """
    additional_minutes = minutes - 50
    additional_text = text_messages - 50
    recharge_min = additional_minutes * 0.25
    recharge_text = additional_text * 0.15
    total = 15.00 + recharge_min + recharge_text + 0.44
    tax = total * 0.05

    print('Your Cellphone bill is:')
    print('Base Charge: 15.00')
    print('Additional minutes: ' + str(round(additional_minutes,0)))
    print('Charge for additional minutes: ' + str(round(recharge_min,2)))
    print('Additional Text-messages: ' + str(round(additional_text,0)))
    print('Charge of additional text-messages: ' + str(round(recharge_text,2)))
    print('The 911 support: 0.44')
    print('The tax 5%:' + str(round(tax,2)))
    print('The total is: ' + str(round((total + tax),2)))

elif minutes > 50 and  text_messages < 50:
    additional_minutes = minutes - 50
    recharge_min = additional_minutes * 0.25
    total = 15.00 + recharge_min + 0.44
    tax = total * 0.05
    print('Your Cellphone bill is: ')
    print('Addtional minutes: ' + str(round(additional_minutes,0)))
    print('Charge for additional minutes: ' + str(round(recharge_min,2)))
    print('The 911 support: 0.44')
    print('The tax 5%: ' + str(round(tax,2)))
    print('The total is: ' + str(round((total + tax),2)))

elif minutes < 50 and text_messages > 50:
    additional_text = text_messages - 50
    recharge_text = additional_text * 0.15
    total = 15.00 + recharge_text + 0.44
    tax = total * 0.05
    print('Your Cellphone bill is: ')
    print('Additional Text-Messages: ' + str(round(additional_text,0)))
    print('Charge for text messages:  ' + str(round(recharge_text,2)))
    print('The 911 support: 0.44')
    print('The tax 5%: ' + str(round(tax,2)))
    print('The total is: ' + str(round((total + tax),2)))

else:
    total = 15.00 + 0.44
    tax = total * 0.05
    print('Your Cellphone bill is: ')
    print('The 911 support: 0.44')
    print('The tax 5%: ' + str(round(tax,2)))
    print('The total is: ' + str(round((total + tax),2)))


###
