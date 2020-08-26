#!/usr/bin/env python3
import sys
import os
import re
import operator

def clean_list(list_word):

    c = []
    for word in list_word:
        if '\n' in word:
            c += word.split('\n')
            list_word.remove(word)
    list_word += c
    list_word.remove('')
    return list_word

words, word_len = {} , {}
filename = sys.argv[1]

with open(filename) as file:
    text = file.read()
    list_word = text.split(" ")
    list_word = clean_list(list_word)

    for word in list_word:
        words[word] = list_word.count(word)

    file.close()

for key in words.keys():
    word_len[key] = len(key)
word_len = dict(sorted(word_len.items(),key=operator.itemgetter(1),reverse=True))


print("{:>20}    {:>20}".format("Word","Len"))
for key, value in word_len.items():
    print("{:>20}  {:>20}".format(key,value))
