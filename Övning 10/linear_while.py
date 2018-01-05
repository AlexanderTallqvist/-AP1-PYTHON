'''
linear_while.py
Linda Mannila 2010
Demonstrates linear_search, implemented with a while loop.
'''
def linear_search(mylist, x):
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


def main():
    lista = range(100000)
    index = linear_search(lista, 7000)
    if index == -1:
        print "Element not found"
    else:
        print "Element found in index %d" % index
