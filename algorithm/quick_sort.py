def pivot(arr, left, right):
    pivot_idx = left
    pivot_value = arr[left]

    for i in range(left + 1, right + 1): # loop from start + 1 to end
        if arr[i] < pivot_value:
            pivot_idx += 1
            [arr[pivot_idx], arr[i]] = [arr[i], arr[pivot_idx]]

    [arr[left], arr[pivot_idx]] = [arr[pivot_idx], arr[left]]

    return pivot_idx

# print(pivot([5, 2, 1, 8, 4, 7, 6, 3], 0, 7))
# print(pivot([32, 29, 15, 7], 0, 3))


def quick_sort(arr, left, right):
    if left < right:
        pivot_idx = pivot(arr, left, right)
        quick_sort(arr, left, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, right)

    return arr


print(quick_sort([5, 2, 1, 8, 4, 7, 6, 3], 0, 7))
print(quick_sort([32, 29, 15, 7], 0, 3))
print(quick_sort([32, 1, 2, 3], 0, 3))
print(quick_sort([32, 1, 15, 2, 3], 0, 4))
print(quick_sort([1, 2, 3, 4, 5], 0, 4))
