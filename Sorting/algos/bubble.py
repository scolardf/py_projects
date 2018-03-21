import time as t

# Bubble Sort Algorithm
# - Prints swaps to list as they occur
def bubble(l):
    for n in range(len(l) - 1, 0, -1):
        for i in range(n):
            if l[i] > l[i + 1]:
                l[i + 1], l[i] = l[i], l[i + 1]
                print(f"Bubble:{l}")
                t.sleep(.01)
