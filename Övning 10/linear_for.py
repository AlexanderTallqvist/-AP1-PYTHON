

import random

def binary_search(mylist, target):

    # Get start and end values of array
    start = 0
    end = len(mylist) - 1

    while start <= end:
        mid = (start + end) / 2 # Calculate midpoint
        if mylist[mid] == target:
            return mid # Key found at index mid
        # Determin which subarray to search
        elif target < mylist[mid]:
            end = mid - 1 # Change end index to serch lower subarray
        else:
            start = mid + 1 # Change start index to serch upper subarray
    return -1 # Return -1 if index is not found

def binary_main():
    # Setup list with random integers
    mylist = []

    for x in range(10000):
        mylist.append(random.randrange(1, 100000))

    # Sort the list of random integers
    mylist.sort()
    index = binary_search(mylist, 5000)
    if index == -1:
        return "Element not found"
    else:
        return "Element found in index %d" % index


def linear_search(mylist, x):

    # Get the lenght of our list
    numelem = len(mylist) - 1

    # Loop through each item in the list.
    # Stop looping and return the index if the desired item is found
    for index in range(0, numelem):
        if x == mylist[index]:
            return index

    # The element was not found. Return -1
    return -1

def linear_main():

    # Setup list with random integers
    mylist = []

    for x in range(10000):
        mylist.append(random.randrange(1, 100000))

    mylist.sort()

    # Check if a specific integer exists using linear search
    index = linear_search(mylist, 5000)
    if index == -1:
        return "Element not found"
    else:
        return "Element found in index %d" % index


import time

def compare_sorts():


    binary_t1 = time.clock()
    sorted_binary = binary_main()
    binary_t2 = time.clock()

    print sorted_binary

    linear_t1 = time.clock()
    sorted_linear = linear_main()
    linear_t2 = time.clock()

    print sorted_linear

    print "Algorithm\tSize \tTime (ms)"
    print "Binary Search\t", 10000, "\t", (binary_t2 - binary_t1)
    print "Linear Search\t", 10000, "\t", (linear_t2 - linear_t1)


compare_sorts()

# Prints
#
# Element not found
# Element not found
#
# Algorithm       Size    Time (ms)
# Binary Search   10000   0.0157769165078
# Linear Search   10000   0.0204816201038
