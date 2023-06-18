import random

def count_inv(arr, length):
    if length <= 1:
        return (arr, 0)
    else:
        half = length // 2
        left, left_inv = count_inv(arr[:half], half)
        right, right_inv = count_inv(arr[half:], length - half)
        sorted_arr, total_inv = count_split_inv(left, right)
        return (sorted_arr, left_inv + right_inv + total_inv)

def count_split_inv(left, right):
    i = 0
    j = 0
    inversion = 0
    new_arr = [0] * (len(left) + len(right))
    for k in range(len(left) + len(right)):
        if i >= len(left):
            new_arr[k] = right[j]
            j += 1
        elif j >= len(right):
            new_arr[k] = left[i]
            i += 1
        else:
            if left[i] <= right[j]:
                new_arr[k] = left[i]
                i += 1
            else:
                new_arr[k] = right[j]
                j += 1
                inversion += len(left) - i
    return new_arr, inversion

with open("test.txt", 'r') as test:
    arr = [int(x.strip()) for x in test]
    print(count_inv(arr, len(arr))[1])