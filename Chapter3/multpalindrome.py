def mult_palindrome(s):
    """Determina si una cadena es palindrome"""
    cp = s.split()
    s = ''.join(cp)
    cp = []
    for i in s:
        cp.append(i)
    cp.reverse()
    cps = ''.join(cp)

    if cps == s:
        return 'Palindrome'
    else:
        return 'No es palindrome'

if __name__=='__main__':
    s = input("Introduzca el string: ")
    print(mult_palindrome(s))
