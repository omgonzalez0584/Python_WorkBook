#Exercise 56:  Cellphone bill.

print('The programa calculate a Cellphone Bill.')
minutes = float(input('Input the amount of minutes: '))
text_messages = float(input('Input the amount of text-messages: '))

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
    print('Additional minutes: ' + str(additional_minutes))
    print('Charge for additional minutes: ' + str(recharge_min))
    print('Additional Text-messages: ' + str(additional_text))
    print('Charge of additional text-messages: ' + str(recharge_text))
    print('The 911 support: 0.44')
    print('The tax 5%:' + str(tax))
    print('The total is: ' + str(total + tax))

elif minutes > 50 and  text_messages < 50:
    additional_minutes = minutes - 50
    recharge_min = additional_minutes * 0.25
    total = 15.00 + recharge_min + 0.44
    tax = total * 0.05
    print('Your Cellphone bill is: ')
    print('Addtional minutes: ' + str(additional_minutes))
    print('Charge for additional minutes: ' + str(recharge_min))
    print('The 911 support: 0.44')
    print('The tax 5%: ' + str(tax))
    print('The total is: ' + str(total + tax))

elif minutes < 50 and text_messages > 50:
    additional_text = text_messages - 50
    recharge_text = additional_text * 0.15
    total = 15.00 + recharge_text + 0.44
    tax = total * 0.05
    print('Your Cellphone bill is: ')
    print('Additional Text-Messages: ' + str(additional_text))
    print('Charge for text messages:  ' + str(recharge_text))
    print('The 911 support: 0.44')
    print('The tax 5%: ' + str(tax))
    print('The total is: ' + str(total + tax))

else:
    total = 15.00 + 0.44
    tax = total * 0.05
    print('Your Cellphone bill is: ')
    print('The 911 support: 0.44')
    print('The tax 5%: ' + str(tax))
    print('The total is: ' + str(total + tax))
