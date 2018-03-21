import time as t

# Quicksort Algorithm
def quick(l):
    print(f"- List: {l}")
    les = []
    equ = []
    grt = []
    if len(l) > 1:
        pivot = l[0]
        for x in l:
            if x < pivot:
                les.append(x)
            elif x > pivot:
                grt.append(x)
            else:
                equ.append(x)
        newL = quick(les) + equ + quick(grt)
        print(f"Returning {newL}")
        t.sleep(0.01)
        return newL
    else:
        print(f"Returning {l}")
        return l
