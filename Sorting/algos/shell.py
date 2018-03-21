import time as t

# Shell sort algorithm
def shell(l):
    gap = len(l) // 2

    while gap > 0:
        print(f"Shell:Gap is {gap}")
        for i in range(gap):
            for j in range(i + gap, len(l), gap):
                val = l[j]
                pos = j
                while pos >= gap and l[pos - gap] > val:
                    l[pos] = l[pos - gap]
                    pos = pos - gap
                    print(f"Shell:{l}")
                    t.sleep(.1)
                l[pos] = val
            print(f"Shell:{l}")
            t.sleep(.1)
        gap //= 2
