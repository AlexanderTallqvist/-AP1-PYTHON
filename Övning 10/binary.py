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

def main():
    mylist = [2,4,6,7,8,9,11,14,21,28,33,35,39]
    index = binary_search(mylist, 12)
    if index == -1:
        print "Element not found"
    else:
        print "Element found in index %d" % index
