#!/bin/python3

import sys

#https://www.hackerrank.com/challenges/compare-the-triplets

# Read from input
Alice = [int(arr_temp) for arr_temp in input().strip().split(' ')]
Bob = [int(arr_temp) for arr_temp in input().strip().split(' ')]

#Calculate score
AliceScore = len([1 for a,b in zip(Alice,Bob) if a>b])
BobScore = len([1 for a,b in zip(Alice,Bob) if a<b])

print(AliceScore, BobScore)
