def merge_arr(arr1, arr2):
    new_arr = []
    length_arr1 = len(arr1)
    length_arr2 = len(arr2)
    idx_arr1 = 0
    idx_arr2 = 0
    min_value = None

    while idx_arr1 < length_arr1 and idx_arr2 < length_arr2:
        if arr1[idx_arr1] < arr2[idx_arr2]:
            min_value = arr1[idx_arr1]
            idx_arr1 += 1
        else:
            min_value = arr2[idx_arr2]
            idx_arr2 += 1
        new_arr.append(min_value)
    
    while idx_arr1 < length_arr1:
        min_value = arr1[idx_arr1]
        idx_arr1 += 1
        new_arr.append(min_value)

    while idx_arr2 < length_arr2:
        min_value = arr2[idx_arr2]
        idx_arr2 += 1
        new_arr.append(min_value)

    return new_arr

print(merge_arr([1, 10, 50], [2, 14, 99, 100]))
print(merge_arr([], [1, 3]))