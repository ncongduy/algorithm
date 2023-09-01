def bubble_sort(arr): 
    length = len(arr)

    for i, it in enumerate(arr):
        for j, jt in enumerate(arr):
            if j == length - 1:
                continue

            if(arr[j] > arr[j+1]):
                print(f'{arr[j]} - {arr[j+1]}')
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp

    return arr


print(bubble_sort([32, 29, 15, 7, 5]))
