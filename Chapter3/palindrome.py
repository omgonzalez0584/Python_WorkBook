def palindrome(s):
    cp = []
    for  i in s:
        cp.append(i)
    cp.reverse()
    copia = ''.join(cp)
    if copia == s:
        return 'Es palindrome'
    else:
        return 'No es palindrome'


if __name__=='__main__':
    s = input("Introduzca el string: ")
    print(palindrome(s))
