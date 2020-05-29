
if __name__=='__main__':
    cost_group = 0
    guest_ages = []

    while True:
        age = input("Introduzca la edad del visitante: ")
        if age == '':
            break
        else:
            guest_ages.append(int(age))

    for i in guest_ages:
        if i >= 3 and i <= 12:
            cost_group += 14.00
        elif i > 65:
            cost_group += 18.00
        else:
            cost_group += 23.00

    print("Costo del grupo de vistantes es: %.2f"  %cost_group)
