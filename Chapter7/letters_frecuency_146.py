#!/usr/bin/env python3

import re
import sys
import operator
import os

filename = sys.argv[1]
letters = {}
if os.path.exists(filename):
    with open(filename) as file:
        text = file.read()
        for letter in text:
            if re.match(r"[^.? ,;!'\d]",letter):
                letters[letter] = text.count(letter)

    file.close()

    letters = dict(sorted(letters.items(),key=operator.itemgetter(1),reverse=True))
    count = 0
    for key, value in letters.items():
        if count == 5:
            break
        else:
            print("[{}]={}".format(key,value))
            count+=1
else:
    print("Error, archivo no existe")
