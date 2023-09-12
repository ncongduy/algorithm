#####################################################################
## from Udemy
##############
# import math

# def get_digit(num, i):
#     return math.floor(num / math.pow(10, i)) % 10

# def digit_count(num):
#     if num == 0:
#         return 1
#     return math.floor(math.log10(num)) + 1
######################################################################

## do by my selft
def get_digit(num, i):
    num1_str = str(num)
    if i >= len(num1_str):
        return 0
    return int(num1_str[len(num1_str) - 1 - i])

def digit_count(num):
    num_str = str(num)
    return len(num_str)

def most_digit(arr):
    max_val = 0
    for i in arr:
        max_val = max(max_val, digit_count(i)) 
    return max_val 

# print(get_digit(12345, 0)) # 5
# print(get_digit(12345, 1)) # 4

# print(digit_count(1)) # 1
# print(digit_count(25)) # 2

# print(most_digit([1234, 56, 7])) # 4
# print(most_digit([1, 11, 11111])) # 5

def radix_sort(arr):
    most_digit_count = most_digit(arr)

    for i in range(most_digit_count):
        digit_bucket = [[] for j in range(10)]

        for k in range(len(arr)):
            digit = get_digit(arr[k], i)
            digit_bucket[digit].append(arr[k])

        arr = []
        for item in digit_bucket:
            arr += item

        print(digit_bucket)
        print(arr)
        print('---')
        
    return arr

print(radix_sort([12, 9862, 23, 345, 2345, 5476]))