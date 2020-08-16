#!/usr/bin/env python3

def formating_list(string):
    cadena = ''
    if len(string) == 2:
        return string[0] + " and " + string[1]
    elif len(string) == 1:
        return str(string[0])
    else:
        for i in string:
            if string.index(i) == (len(string) - 1):
                cadena += string[-2] + " and " + string[-1]
                break
            cadena += i + ', '
        return cadena

def main():
    string = input().split()
    print(formating_list(string))
main()
