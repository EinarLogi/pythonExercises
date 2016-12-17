#!/bin/python3

import sys

#https://www.hackerrank.com/challenges/diagonal-difference

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

d1 = [] # to hold diagonal values from top left to bottom right
d2 = [] # to hold diagonal values form top right to bottom left
i = 0 # iterator
j = n-1 # iterator
for numberList in a:
    d1.append(numberList[i])
    d2.append(numberList[j])
    i = i + 1
    j = j - 1
print(abs(sum(d1)- sum(d2)))
