#!/usr/bin/env python3

morse_letters = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.',
                'G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..',
                'M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.',
                'S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-',
                'Y':'-.--','Z':'--..','0':'-----','1':'.----','2':'..---',
                '3':'...--','4':'....-','5':'.....','6':'-....','7':'--...',
                '8':'---..','9':'----.'}

translate = ''
string = input('Write the message: ')
for i in string:
    if i.upper() in morse_letters:
        translate +=morse_letters[i.upper()]

print(translate)
