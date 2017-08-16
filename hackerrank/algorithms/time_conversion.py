#!/bin/python3

# https://www.hackerrank.com/challenges/time-conversion
import sys

def timeConversion(s):
    # Complete this function
    ar = s.split(':')
    tail = ar[-1][-2:].lower()
    addition_hours = 0
    if (tail == 'pm' and ar[0] != '12') or (tail == 'am' and ar[0] == '12'):
    	addition_hours = 12
    hh = int((int(ar[0]) + addition_hours) % 24)
    new_time = "%02d:" % hh
    new_time += ':'.join(ar[1:])
    new_time = new_time[:-2]
    return new_time
     
s = input().strip()
result = timeConversion(s)
print(result)