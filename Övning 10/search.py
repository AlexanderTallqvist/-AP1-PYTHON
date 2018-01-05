'''
search.py
Collection of search functions
'''

def linear_search_for(mylist, x):
    '''Using linear search, returns some i such that mylist[i] == x.
       If x is not in mylist, then -1 is returned. '''

    # number of elements in mylist, i.e. last index + 1
    numelem = len(mylist)
    
    # create a list of all indices so that they can be traversed by a for-loop
    indices = range(numelem)

    for index in indices:
        if x == mylist[index]:
            return index

    # if we get to this line of code, the element has not been found
    return -1

def linear_search_while(mylist, x):
    '''Using linear search, returns some i such that mylist[i] == x. If x is
    not in mylist, then -1 is returned.
    '''
    index = 0

    # Run the loop as long as the index is 0,1,2...,len(lst)-1
    while index < len(mylist):
        # If x is found, return the corresponding index
        if x == mylist[index]:
            return index
        # Increment index for each iteration, otherwise we get an infinite loop
        index += 1

    # If we get to this line of code, x is not in mylist    
    return -1

def binary_search(mylist, x):
    ''' Using binary search, returns some i such that mylist[i] == x.  If
    x is not in mylist, then -1 is returned. IMPORTANT: elements of mylist
    must be in ascending sorted order!

    Binary search is an important algorithm because it is extremely
    efficient: for a sequence of length n, it does, at *worst*, about log
    n iterations of the loop. So, for example, a list of a million
    items will require about 20 comparisons in the worst case.
    '''
    begin = 0
    end = len(mylist) - 1
    
    while begin <= end:
        mid = (begin + end) / 2
        if mylist[mid] == x:
            return mid
        elif x < mylist[mid]:
            end = mid - 1
        else:
            begin = mid + 1
    return -1








