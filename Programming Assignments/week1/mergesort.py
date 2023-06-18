import random 

def merge_sort(arr):
    n = len(arr)
    half = n // 2
    if (n <= 1):
        return arr
    left_sorted = merge_sort(arr[:half])
    right_sorted = merge_sort(arr[half:])
    return merge(left_sorted, right_sorted)

def merge(left, right):
    i = 0
    j = 0
    n = len(left) + len(right)
    new_arr = [0] * n
    for k in range(n):
        if i == len(left):
            new_arr[k] = right[j]
            j += 1
        elif j == len(right):
            new_arr[k] = left[i]
            i += 1
        else:
            if left[i] > right[j]:
                new_arr[k] = right[j]
                j += 1
            else:
                new_arr[k] = left[i]
                i += 1
    return new_arr

def test_merge_sort():
    # tests the merge_sort algorithms
    result = 0
    test_arr = [random.randint(0, 1000) for _ in range(100000)]
    return merge_sort(test_arr) == sorted(test_arr)