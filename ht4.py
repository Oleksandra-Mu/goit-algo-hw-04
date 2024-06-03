import timeit
import random

def implementation_time(func, data):
    start_time = timeit.default_timer()
    func(data)
    execution_time = timeit.default_timer() - start_time
    return execution_time

# Сортування злиттям
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


# Сортування вставками
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key
    return lst

def timsort(data):
    return sorted(data)

array10 = random.sample(range(100000), 10)
array100 = random.sample(range(100000), 100)
array1000 = random.sample(range(100000), 1000)
array10000 = random.sample(range(100000), 10000)
    
test_data = [array10, array100, array1000, array10000]
functions = [merge_sort, insertion_sort, timsort]

header = "{:<20}|{:<20}|{:<20}|{:<20}|{:<20}".format("Sorting Algorithm", "Array 10", "Array 100", "Array 1000", "Array 10000")
print(header)

for function in functions:
    row = "{:<20}".format(function.__name__)
    for array in test_data:
        execution_time = implementation_time(function, array)
        row += "|{:<20.5f}".format(execution_time)
    print(row)
