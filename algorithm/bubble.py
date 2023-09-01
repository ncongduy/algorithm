def bubble_sort(arr): 
    length = len(arr)

    for i, it in enumerate(arr):
        swap = False
        for j, jt in enumerate(arr):
            if j == length - 1:
                break

            print(f'{arr} - {arr[j]} - {arr[j+1]}')

            if(arr[j] > arr[j+1]):
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp
                swap = True
            
        if not swap:
            break

    return arr


# print(bubble_sort([32, 29, 15, 7]))
# print(bubble_sort([32, 1, 2, 3]))
# print(bubble_sort([32, 1, 15, 2, 3]))
# print(bubble_sort([1, 2, 3, 4, 5]))

# O(n^2)
