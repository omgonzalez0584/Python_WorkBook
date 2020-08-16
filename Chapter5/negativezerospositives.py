#!/usr/bin/env python3

negatives, zeros, positives = [] , [] , []
numbers = list(map(int,input().split()))

for i in numbers:
    if i < 0:
        negatives.append(i)
    elif i > 0:
        positives.append(i)
    else:
        zeros.append(i)

numbers = negatives +  zeros + positives
print(numbers)
