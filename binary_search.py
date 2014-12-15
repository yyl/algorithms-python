#!/usr/bin/python
import time
import random
import bisect

# given sorted list l
# find the item with value k
# discard half of list each time
# log(n)
def binary_search(l, k):
    start = 0
    end = len(l) - 1
    mid = end/2
    while end > start and start != mid and end != mid:
        if l[mid] == k:
            break
        elif l[mid] > k:
            end = mid
        else:
            start = mid
        # if not met
        # return largest one smaller than k
        mid = (start + end)/2
        # return smallest one larger than k
        # mid = 1 + (start + end)/2
    return mid
k = 2
l = [1,3]

#print l
start = time.time()
print binary_search(l, k)
print time.time() - start
start = time.time()
print bisect.bisect_left(l, k)
print time.time() - start
