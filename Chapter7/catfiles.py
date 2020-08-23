#!/usr/bin/env python3

import os
import sys

filenames = sys.argv[1:]
content = []

for i in filenames:
    if os.path.exists(i):
        with open(i) as file:
            lines = file.readlines()
            content += lines
    else:
        print("El archivo {} no existe".format(i))

for lines in content:
    print(lines)
