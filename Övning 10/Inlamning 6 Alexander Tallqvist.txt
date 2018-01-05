# -*- coding: cp1252 -*-
# Inlämning 6 | Uppg. 1, 2, 3
# Alexander Tallqvist


# Uppg. 1

def bubble_sort(list_to_sort):
    # Bubblesort compares n > n+1, and swaps the values if true.
    # Bubblesort continues until the list is sorted from smallest to largest

    list_sorted = False
    lenght = len(list_to_sort) - 1

    while not list_sorted:
       list_sorted = True
       for i in range(lenght):
           if list_to_sort[i] > list_to_sort[i+1]:
               list_sorted = False
               temp_item = list_to_sort[i]
               list_to_sort[i] = list_to_sort[i+1]
               list_to_sort[i+1] = temp_item

    return list_to_sort

our_list = [1,4,16,2,23,11,47,3,99,0]
sorted_list = bubble_sort(our_list)
print(sorted_list)


# Uppg. 2

import time

def compare_sorts(list_to_sort):

    # Function that is used to compare the speed of our custom
    # Bubblesort, and Pythons built-in .sort() method.

    bubble_t1 = time.clock()
    sorted_bubble = bubble_sort(list(list_to_sort))
    bubble_t2 = time.clock()

    python_t1 = time.clock()
    sorted_python = list_to_sort.sort()
    python_t2 = time.clock()

    print "Algorithm\tSize \tTime (ms)"
    print "Bubble Sort\t", len(list_to_sort), "\t", (bubble_t2 - bubble_t1)
    print "Python Sort\t", len(list_to_sort), "\t", (python_t2 - python_t1)


our_list_1 = [1,4,16,2,23,11,47,3,99,0]
our_list_2 = [1,4,16,2,23,11,47,3,99,0,1,4,16,2,23,11,47,3,99,0,1,4,16,2,23,11,47,3,99,0]
compare_sorts(our_list_2)


# Uppg. 3 | B

def file_check(file_name):
    try:
      open(file_name, "r")
      return True

    except IOError:
      print "Error: File does not appear to exist."
      return False


def file_to_list(file_name):

    # Function that reads in numbers from an external file,
    # appends the numbers to a list, and finaly uses Bubblesort
    # to sort the list

    if file_check(file_name):
        file_to_read = open(file_name, "r")
        file_list = []

        for line in file_to_read.readlines():
            nmbr = int(line)
            file_list.append(nmbr)

        file_to_read.close()

        return file_list

new_file_list = bubble_sort(file_to_list("data.txt"))

print new_file_list
