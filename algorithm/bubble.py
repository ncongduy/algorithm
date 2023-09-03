def bubble_sort(arr): 
    size = len(arr)

    for i in range(size):
        swap = False
        for j in range(size):
            if j == size - 1:
                break

            print(f'{arr} - {arr[j]} - {arr[j+1]}')

            if(arr[j] > arr[j+1]):
                # swap
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp
                swap = True
            
        if not swap:
            break

    return arr


print(bubble_sort([32, 29, 15, 7]))
# print(bubble_sort([32, 1, 2, 3]))
# print(bubble_sort([32, 1, 15, 2, 3]))
# print(bubble_sort([1, 2, 3, 4, 5]))

# O(n^2)
