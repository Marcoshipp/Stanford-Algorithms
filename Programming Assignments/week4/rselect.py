# takes an array arr,
#       a length n,
#       index i
# outputs:
#   the ith smallest element in the array
import random

def Rselect(arr, n, i):
    if n == 1:
        return arr[0]
    else:
        pIdx = random.randint(0, n - 1)
        # m is where the pivot ended up at
        j = partition(arr, pIdx)
        if j == i:
            return arr[j]
        # i is on the left side of the array
        elif j > i:
            return Rselect(arr[:j], j, i)
        else:
            return Rselect(arr[j + 1:], n - j - 1, i - j - 1)


def partition(arr, pIdx):
    pivot = arr[pIdx]
    arr[0], arr[pIdx] = arr[pIdx], arr[0]
    i = 0
    for j in range(i + 1, len(arr)):
        if pivot > arr[j]:
            arr[j], arr[i + 1] = arr[i + 1], arr[j]
            i += 1
    arr[i], arr[0] = arr[0], arr[i]
    return i

arr = [random.randint(0, 100) for _ in range(100)]
print(sorted(arr)[10])
print(Rselect(arr, len(arr), 10))