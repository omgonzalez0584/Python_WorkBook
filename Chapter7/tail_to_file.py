#!/usr/bin/env python3
import sys
import os

def tail(lines,line_amount):
    for line in range((len(lines) -line_amount),len(lines)):
        print(lines[line])

filename = sys.argv[1]
line_amount = int(sys.argv[2])

if os.path.exists(filename):
    with open(filename,'r') as file:
        lines =  file.readlines()
        tail(lines,line_amount)

    file.close()
else:
    print('El archivo no existe.')
