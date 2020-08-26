#!/usr/bin/env python3
import os
import re
import sys

filename = sys.argv[1]
number = 1
new_content = []
if os.path.exists(filename):
    with open(filename) as file:
        lines =  file.readlines()
        for line in lines:
            new_content.append(str(number)+". "+line )
            number+=1

    file.close()
else:
    print("El archivo no existe")

file_with_lines = 'ln_'+filename
with open(file_with_lines,'w') as file_w:
    for line in new_content:
        file_w.write(line)

    file_w.close()
