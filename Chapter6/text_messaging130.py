#!/usr/bin/env python3

def key_preses(text,keypad):
    """Return the keys pressed on the phone"""
    presses = []
    for char in text:
        for key , value in keypad.items():
            if char in value:
                presses.append(key * (value.index(char) + 1))
                break

    presses = ''.join(presses)
    return presses

keypad = {'1':["." , ',' , "?", "!", ":"],
           '2':['A','B','C'],'3':['D','E','F'],
           '4':['G','H','I'],'5':['J','K','L'],
           '6':['M','N','O'],'7':['P','Q','R','S'],
           '8':['T','U','V'],'9':['W','X','Y','Z'],
           '0':' '}

print("Key Pressed: {}".format(key_preses(input('Write the Message: ').upper(),keypad)))
