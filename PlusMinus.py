#!/bin/python3

import sys

# https://www.hackerrank.com/challenges/plus-minus

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
numberArray = [0,0,0] # positive, negative, zero
for number in arr:
    if number > 0:
        numberArray[0] = numberArray[0] + 1
    elif number < 0:
        numberArray[1] = numberArray[1] + 1
    else:
        numberArray[2] = numberArray[2] + 1

for item in numberArray:
    print('{0:16f}'.format(item / n).strip())
