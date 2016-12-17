#!/bin/python3

import sys

#https://www.hackerrank.com/challenges/staircase?h_r=next-challenge&h_v=zen

n = int(input().strip())

whitespaceCounter = n-1
whitespace = ' '

for i in range(1,n+1):
    print(whitespace*whitespaceCounter + "#"*i)
    whitespaceCounter -= 1
