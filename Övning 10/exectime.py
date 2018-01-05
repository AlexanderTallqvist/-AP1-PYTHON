import time
import linear_while

mylist= range(10000000)

# t1 contains the starting time (in seconds)
t1 = time.clock()
# Execute the function
linear_while.linear_search(mylist, 7500000)
# t2 contains the finishing time (in seconds)
t2 = time.clock()

# Calculates the execution time (in seconds)
exectime = t2-t1

# Prints the time (in seconds and milliseconds)
print "Executed in %0.4f seconds" % exectime
print "Executed in %0.4f milliseconds" % (exectime * 1000)
