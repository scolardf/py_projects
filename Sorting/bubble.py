import time as t
import random as r
import sys

# Bubble Sort Example
# - Generates list of integers, shuffles them, then sorts using Bubble Sort
# - Takes 1 argument, integer defining size of list

# algorithm
def bubble(l):
	for n in range(len(l)-1,0,-1):
		for i in range(n):
			if l[i] > l[i+1]:
				l[i+1], l[i] = l[i], l[i+1]
				print(l)
				t.sleep(.01)


# Create list of numbers
size = sys.argv[1]
myList = list(range(int(size)))
print(f"List of size {size} \n{myList}")
t.sleep(.5)
r.shuffle(myList)
print(f"- List shuffled\n{myList}")
t.sleep(.5)

bubble(myList)