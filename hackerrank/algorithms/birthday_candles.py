#!/bin/python3
# https://www.hackerrank.com/challenges/birthday-cake-candles

import sys

def birthdayCakeCandles(n, ar):
    maxn = 0
    countn = 0
    for i in range(0,n):
    	if ar[i] > maxn:
    		countn = 1
    		maxn = ar[i]
    	elif ar[i] == maxn:
    		countn += 1
    return countn

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)