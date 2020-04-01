def date_to_numbers(month, day):
    """Funcion convierte un mes y dia a un numero de los 365 dias"""
    months_dict = {'enero':1,'febrero':2,'marzo':3,'abril':4,'mayo':5,
                'junio':6,'julio':7,'agosto':8,'septiembre':9,
                'octubre':10,'noviembre':11,'diciembre':12}

    days_list = [31,29,31,30,31,30,31,31,30,31,30,31]

    if months_dict[month] == 1:
        return day
    else:
        number = day
        for i in range(months_dict[month] - 1):
            number += days_list[i]
        return number
