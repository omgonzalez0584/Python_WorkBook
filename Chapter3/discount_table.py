#Exercise 62: Discount Table

#Listado de precios.
price_list = [4.95 , 9.95 , 14.95 , 19.95 , 25.95]
discount = 0

#Ciclo for para generar la lista de precios.
for i in price_list:
    discount = i * 0.60
    price_discount = i - discount
    print('Original price: ' + str(i) + ' | ' + 'Discount: 60% ' +
            'New Price: ' + str(round(price_discount,2)))
