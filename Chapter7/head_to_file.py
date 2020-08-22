#!/usr/bin/env python3
import sys

filename = sys.argv[1]
count_lines = sys.argv[2]

with open(filename,'r') as f:
    lines = f.readlines()
    if int(count_lines) < len(lines):
        for line in range(len(lines)):
            if line == int(count_lines):
                break
            else:
                print(lines[line])
    else:
        for line in lines:
            print(line)
    f.close()
