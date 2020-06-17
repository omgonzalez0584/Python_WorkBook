#Exercise 70 Caesar Cipher

def cipher(s):
    """Funcion que realizar cifrado de la cadena """

    #Diccionario que realizar convertir las 3 ultimas letras
    last_letter = {'x':'a','y':'b','z':'c','X':'A','Y':'B','Z':'C'}
    cipher_list = []
    for i in s:
        if i in last_letter:
            cipher_list.append(last_letter[i])
        elif i == ' ':
            cipher_list.append(i)
        else:
            cipher_list.append(chr(int(ord(i))+3))

    return ''.join(cipher_list) #Devuelve el string encriptado

if __name__=='__main__':
    s = input('Introduzca la cadena: ') #Introduciendo cadena
    s = cipher(s) #LLamada a la funcion
    print(s)
