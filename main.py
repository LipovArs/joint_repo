def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap

        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heapify(arr, i, 0)

arr = [2, 1, 4, 5, 6, 7, 10, 15, 'cat', 'apple', 'ball', 'duck', 'frog', 'eagle', 'green', 25, 17, 8]

# Split the list into numbers and strings and sort separately
numbers = [x for x in arr if isinstance(x, int)]
strings = [x for x in arr if isinstance(x, str)]

heapSort(numbers)
strings.sort()  # Alphabetical sorting for strings

# Join the two sorted lists again
arr = numbers + strings

print('Sorted array is')
for i in arr:
    print(i)


