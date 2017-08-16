#!/bin/python3
# https://www.hackerrank.com/challenges/insertion-sort
# Using: Binary Index Tree (BIT): https://www.hackerrank.com/topics/binary-indexed-tree

import sys

def insertionSortAdv(n, arr):
    # Complete this function
    size = 10**7+1
    bit = [0] * size
    res = 0
    for val in reversed(arr):
        # set/update
        idx = val
        while (idx <= size):
            bit[idx] += 1
            idx += (idx & -idx)
        # get/read/sum
        idx = val-1
        while (idx > 0):
            res += bit[idx]
            idx -= (idx & -idx)
    return res


T = int(input().strip())
for i in range(T):
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = insertionSortAdv(n, arr)
    print(result)