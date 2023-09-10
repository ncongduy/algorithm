import math 

def merge_arr(arr1, arr2):
    sorted_arr = []
    i = 0   # index of arr1
    j = 0   # index of arr2
    min_value = None

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            min_value = arr1[i]
            i += 1
        else:
            min_value = arr2[j]
            j += 1
        sorted_arr.append(min_value)
    
    while i < len(arr1):
        min_value = arr1[i]
        i += 1
        sorted_arr.append(min_value)

    while j < len(arr2):
        min_value = arr2[j]
        j += 1
        sorted_arr.append(min_value)

    return sorted_arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = math.floor(len(arr)/2)
    left_arr = merge_sort(arr[slice(0, mid)])
    right_arr = merge_sort(arr[slice(mid, len(arr))])

    return merge_arr(left_arr, right_arr)

print(merge_sort([1, 10, 30, 50, 2]))
# print(merge_sort([32, 29, 15, 7]))
# print(merge_sort([32, 1, 2, 3]))
# print(merge_sort([32, 1, 15, 2, 3]))
# print(merge_sort([1, 2, 3, 4, 5]))