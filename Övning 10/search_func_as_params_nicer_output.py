'''
search_func_as_params_nicer_output.py
Linda Mannila 2007
Demonstrates how functions can be sent as arguments to another function.
Also introduces the function attribute func_name that contains the name of
the function.
NOTE! This is not required for the course, but aimed at those who are interested
in learning more.
'''

import search

def run_and_time(f, the_list):
    ''' Run and time the execution of function f'''

    import time   
    t1 = time.clock()
    position = f(the_list, 75000)
    t2 = time.clock()

    # Convert from seconds to milliseconds
    exec_time = (t2-t1)*1000

    # Uses the function attribute func_name to access the name of the function
    f_name = f.func_name

    print "%s: %0.4f ms" % (f_name, exec_time)

def test_search_algorithms():
    ''' Tests all search algorithms'''
    
    the_list = range(100000)

    # Creates a list containing the names of the search funtions we have defined
    algorithms = [search.linear_search_for, search.linear_search_while, search.binary_search]

    # Executes the function run_and_time for each algorithm
    # Illustrates how you can send functions as parameters to other functions
    for alg in algorithms:
        run_and_time(alg, the_list)
                
def main():
    ''' Starts the testing'''
    test_search_algorithms()
