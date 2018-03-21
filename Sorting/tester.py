import random as r
import time as t
import sys

# algorithm imports
from algos.bubble import bubble
from algos.quick import quick
from algos.shell import shell

## Tester for different sorting algorithms
# Creates a list of integers, shuffles it, and runs a sorting algorithm on it
# Takes 1 argument, size, which is an Integer defining the size of a list

# Create list of numbers
size = sys.argv[1]
myList = list(range(int(size)))
print(f"List of size {size} \n{myList}")
t.sleep(.5)
r.shuffle(myList)
print(f"- List shuffled\n{myList}")
bubble(myList)

r.shuffle(myList)
print(f"- List shuffled\n{myList}")
myList = quick(myList)
print(f"{myList}")

r.shuffle(myList)
print(f"- List shuffled\n{myList}")
shell(myList)
print(f"{myList}")
