#!/bin/python3
# https://www.hackerrank.com/challenges/fraudulent-activity-notifications

import sys
import math
def insertItem(arr, item):
    first, last = 0, len(arr)
    while first < last:
        mid = (first + last) // 2
        if item < arr[mid]: 
            last = mid
        else:
            first = mid + 1
    arr.insert(first, item)
    return arr

def findTheMedian(n, arr):
    # Complete this function
    mid = n/2
    ceil = math.ceil(mid)
    floor = math.ceil(mid+0.45)
    return (arr[ceil-1] + arr[floor-1])/2

def activityNotifications(expenditure, d):
    # Complete this function
    n = len(expenditure)
    if (n < d + 1):
        return 0
    count = 0
    d_list = []
    for idx in range(n-d):
        d_len = len(d_list)
        for i in range(idx+d_len, idx+d):
            d_list = insertItem(d_list, expenditure[i])
        median = findTheMedian(d, d_list)
        if (median * 2) <= expenditure[idx+d]:
            count += 1
        first = d_list.index(expenditure[idx])
        d_list.pop(first)
    return count

with open('../test_case/fraudulent_notification.txt') as f:
    #n, d = f.read().strip().split(' ')
    #n, d = [int(n), int(d)]
    n, d = 200000, 10122
    expenditure = list(map(int, f.read().strip().split(' ')))
    result = activityNotifications(expenditure, d)
    print(result)