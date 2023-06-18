def quick_sort(arr, l, h, total):
    if h > l:
        total[0] += h - l
        m = partition(arr, l, h, total)
        quick_sort(arr, l, m - 1, total)
        quick_sort(arr, m + 1, h, total)

def choose_median(arr, l, h):
    """
        CHOOSE THE MEDIAN BETWEEN 3 ELEMENTS AS PIVOT
        FROM NAMELY THE FIRST, THE MIDDLE, AND THE FINAL ELEMENT
    """
    length = h - l + 1
    mid = length // 2 - 1 if length % 2 == 0 else length // 2
    first = arr[l]
    second = arr[l + mid]
    third = arr[h]
    if second <= first <= third or third <= first <= second:
        return l
    elif first <= second <= third or third <= second <= first:
        return l + mid
    elif first <= third <= second or second <= third <= first:
        return h
    return None

def partition(arr, l, h, total):
    # the two pointers i, j:
    # i: is the pointer that points to where the pivot should go to
    # j: is the pointer that seperates the unpartitioned and the partitioned
    m = choose_median(arr, l, h)
    arr[l], arr[m] = arr[m], arr[l]
    pivot = arr[l]
    i = l
    for j in range(l + 1, h + 1):
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[l], arr[i] = arr[i], arr[l]
    return i

def test():
    test_arr = []
    with open("test.txt", 'r') as f:
        for line in f:
            test_arr.append(int(line.strip()))
    total = [0]
    quick_sort(test_arr, 0, len(test_arr) - 1, total)
    print(f"Result: {total[0]}")

test()