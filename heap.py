#!/usr/bin/python

# find left child of A[i]
def left(i):
    return 2*i+1

# find right child of A[i]
def right(i):
    return 2*i+2

# keep the max-heap property for A[i] and its children
# O(logn)
def heapify(A, i, heapsize):
    largest = i
    l = left(i)
    r = right(i)
    # check if r and l child is in the heap bounded by heapsize
    if l < heapsize and A[i] < A[l]:
        largest = l
    if r < heapsize and A[largest] < A[r]:
        largest = r
    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        # recursively "push down" the value
        heapify(A, largest, heapsize)

# build a max heap from list A
# O(n)
# bottom-up, in-place
def buildMaxHeap(A):
    # only deal with the first half,
    # as the 2nd half are all leaves
    for i in xrange((len(A)/2) - 1, -1, -1):
        heapify(A, i, len(A))
    return A

# in-place
def heapsort(A):
    # heapsize is used to track remaining items in the heap
    heapsize = len(A)
    sortedA = buildMaxHeap(A)
    # swap last and first in heap, then heapify the 1st one
    for i in xrange(len(sortedA) - 1, 0, -1):
        sortedA[i], sortedA[0] = sortedA[0], sortedA[i]
        heapsize -= 1
        heapify(sortedA, 0, heapsize)
    return sortedA

############
##### priority queue
############
def parent(i):
    if i == 0:
        print "it is already root"
        exit(0)
    if i%2 == 0:
        return (i-2)/2
    else:
        return (i-1)/2

# return the maximum value of the heap
# O(1)
def maximum(heap):
    return heap[0]

# return the maximum item from heap
# remove it from heap
# O(logn)
def extractMax(heap):
    if not heap:
        print "heap underflow"
        exit(0)
    heapsize = len(heap)
    heap[0], heap[heapsize-1] = heap[heapsize-1], heap[0]
    maxh = heap.pop()
    heapsize -= 1
    heapify(heap, 0, heapsize)
    return maxh

# insert the key into the heap
# O(logn)
def heapInsert(heap, key):
    heapsize = len(heap)
    heap.append(key)
    heapsize += 1
    i = heapsize - 1
    while i != 0 and heap[i] > heap[parent(i)]:
        heap[i], heap[parent(i)] = heap[parent(i)], heap[i]
        i = parent(i)

# increase the value of the certain key
# O(logn)
def increaseKey(heap, i, value):
    heapsize = len(heap)
    if i >= heapsize or i < 0:
        print "not in the heap"
        exit(0)
    if value <= heap[i]:
        print "value must be greater than the original"
        exit(0)
    heap[i] = value
    while i != 0 and heap[i] > heap[parent(i)]:
        heap[i], heap[parent(i)] = heap[parent(i)], heap[i]
        i = parent(i)

l = [4,3,2,3,6,2,1,6,8]
print l
print "buildMaxHeap"
h = buildMaxHeap(l)
print h
print "extractMax"
print extractMax(h)
print h
print "heapInsert 10"
heapInsert(h, 10)
print h
print "heapInsert 1"
heapInsert(h, 1)
print h
print "heapInsert 5"
heapInsert(h, 5)
print h
print "increaseKey 2 5"
increaseKey(h, 2, 5)
print h
print "increaseKey 6 10"
increaseKey(h, 6, 10)
print h
