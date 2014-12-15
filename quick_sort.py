#!/usr/bin/python
import time
import random
from collections import deque

# nlogn average, n^2 worst case
# comparison based, not stable
# divide and conquer

# for loop
# filter
# list comprehension
# deque

def quicksort1(unsorted):
    #unsorted = deque(list(unsorted))
    if len(unsorted) <= 1:
        return unsorted
    pivot = unsorted.pop()
    less = [i for i in unsorted if i <= pivot]
    #less = filter(lambda x: x<=pivot, unsorted)
    #greater = filter(lambda x: x>pivot, unsorted)
    greater = [i for i in unsorted if i > pivot]
    #print "array %s: less %s, pivot %s, greater %s" % (unsorted, less, pivot, greater)
    new_less = quicksort(less)
    new_less.append(pivot)
    new_less.extend(quicksort(greater))
    return new_less

def quicksort(unsorted):
    if len(unsorted) <= 1:
        return unsorted
    pivot = unsorted.pop()
    less = [i for i in unsorted if i <= pivot]
    greater = [i for i in unsorted if i > pivot]
    new_less = quicksort(less)
    new_less.append(pivot)
    new_less.extend(quicksort(greater))
    return new_less

# get approximate median of input list
# efficient way to pick pivot
# worst-case O(n)
def medianOfmedian(l):
    length = len(l)
    if length < 5: return l[(length - 1)/2]
    medians = []
    for i in xrange(0, length, 5):
        temp = sorted(l[i:i+5])
        if len(temp) == 5:
            medians.append(temp[2])
        else:
            medians.append(temp[(len(temp)-1)/2])
    return medianOfmedian(medians)

############ in place
def partition(A, p, r):
    pivot = random.randint(p, r)
    A[pivot], A[r] = A[r], A[pivot]
    x = A[r]
    i = p - 1
    for j in xrange(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def qsort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        qsort(A, p, q-1)
        qsort(A, q+1, r)

def quicksort2(unsorted):
    qsort(unsorted, 0, len(unsorted)-1)
    return unsorted

#print quicksort2([4,5,2,7,8,2,5,7,8])
start = time.time()
quicksort2([random.randrange(1000) for i in xrange(100000)])
print "sorted", time.time() - start
