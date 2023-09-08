def insertion_sort(arr):
    size = len(arr)

    if size <= 1:
        return arr

    for i in range(1, size):
        current_value = arr[i]
        j = i - 1 

        while j >= 0 and arr[j] > current_value:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = current_value

    return arr

print(insertion_sort([32, 29, 15, 7]))
print(insertion_sort([32, 1, 2, 3]))
print(insertion_sort([32, 1, 15, 2, 3]))
print(insertion_sort([1, 2, 3, 4, 5]))
print(insertion_sort([2, 1, 9, 76, 4]))

## O(n^2)