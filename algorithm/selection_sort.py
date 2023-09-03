def selection_sort(arr):
    size = len(arr)

    for i in range(size):
        min_index = i

        for j in range(i + 1, size):
            print(f'{arr} - {arr[j]} - {arr[min_index]}')

            if arr[j] < arr[min_index]:
                min_index = j

        if arr[min_index] < arr[i]:
            print("SWAP")
            temp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = temp

    return arr



print(selection_sort([32, 29, 15, 7]))
# print(selection_sort([32, 1, 2, 3]))
# print(selection_sort([32, 1, 15, 2, 3]))
# print(selection_sort([1, 2, 3, 4, 5]))

## O(n^2)