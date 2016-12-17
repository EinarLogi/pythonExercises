#!/bin/python3

import sys

#https://www.hackerrank.com/challenges/a-very-big-sum?h_r=next-challenge&h_v=zen

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
print(sum(arr))
