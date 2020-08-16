#!/usr/bin/env python3

words = []
while True:
    word = input()
    if word == '':
        break
    else:
        if not word in words:
            words.append(word)
print(words)
