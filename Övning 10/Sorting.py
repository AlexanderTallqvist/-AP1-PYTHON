'''
search.py

Collection of search functions
'''


def linear_search_for(mylist, x):

    numelem = len(mylist)

    indices = range(numelem)


    for index in indices:

        if x == mylist[index]:

            return index


    return -1


def linear_search_while(mylist, x):

    index = 0


    while index < len(mylist):

        if x == mylist[index]:

            return index

        index += 1


    return -1


def binary_search(mylist, x):

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
