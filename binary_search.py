# Binary search algorithm
# Uses quick sort for sorting

import numpy as np
from quick_sort import quickSort


def binarySearch(sorted_numbers, integer):
    low = 0
    high = len(sorted_numbers)
    while high >= low:
        mid = (low + high) // 2
        if integer == sorted_numbers[mid]:
            return mid
        elif integer < sorted_numbers[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


if __name__ == "__main__":
    # Random number generation
    print("Binary search algorithm")
    limit = 10
    rand_array = np.random.randint(0, 100, limit)
    print("numbers")
    print(rand_array)
    # sort
    quickSort(rand_array, 0, limit-1)
    print("Sorted array")
    print(rand_array)
    # search
    element = int(input("Enter the number to search: "))
    index = binarySearch(rand_array, element)
    if index != -1:
        print(f"{element} found at index {index} in the sorted array.")
    else:
        print(f"{element} is not in the array.")
