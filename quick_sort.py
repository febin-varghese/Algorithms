# Quick sort algorithm to sort a set of random numbers
# last element is taken as pivot for the implementation
import numpy as np


def partition(numbers, low, high):
    pivot = numbers[high]
    j = low - 1
    for k in range(low, high):
        if numbers[k] < pivot:
            j += 1
            numbers[j], numbers[k] = numbers[k], numbers[j]
    numbers[j+1], numbers[high] = numbers[high], numbers[j+1]
    return j + 1


def quickSort(numbers, low, high):
    if low < high:
        pivot = partition(numbers, low, high)
        quickSort(numbers, low, pivot - 1)
        quickSort(numbers, pivot + 1, high)


if __name__ == "__main__":
    # Random number generation
    limit = 101
    rand_array = np.random.randint(0, 100, limit)
    print("numbers")
    print(rand_array)
    # sort
    quickSort(rand_array, 0, limit-1)
    # check
    sort_bool = True
    for i in range(0, len(rand_array) - 1):
        if rand_array[i + 1] < rand_array[i]:
            sort_bool = False
            break
    if sort_bool:
        print("sorted")
    else:
        print("not sorted")
    print(rand_array)
