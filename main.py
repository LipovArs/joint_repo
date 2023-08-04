def heapify(arr, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # swap
        heapify(arr, i, 0)


def sort_numbers_and_floats(arr):
    numbers = [x for x in arr if isinstance(x, (int, float))]
    heapSort(numbers)
    return numbers


def sort_strings(arr):
    strings = [x for x in arr if isinstance(x, str)]
    strings.sort()
    return strings


arr = [2, 1, 4, 4.5, 5, 6.2, 5, 6, 7, 17.8, 10, 15, 'cat', 'apple', 'pie', 'ball', 'world', 'duck', 'frog', 'eagle', 'green', 25, 3.14,
       17, 8]

sorted_numbers_floats = sort_numbers_and_floats(arr)
sorted_strings = sort_strings(arr)

sorted_arr = sorted_numbers_floats + sorted_strings

print('Sorted array is:')
for item in sorted_arr:
    print(item)

