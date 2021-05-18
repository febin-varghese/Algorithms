# Interpolation search algorithm
# Uses quick sort for sorting

import numpy as np
from quick_sort import quickSort


def interpolationSearch(sorted_numbers, integer, low, high):
    if low <= high and sorted_numbers[low] <= integer <= sorted_numbers[high]:
        numerator = (integer - sorted_numbers[low]) * (high - low)
        denominator = sorted_numbers[high] - sorted_numbers[low]
        position = low + (numerator // denominator)
        if integer == sorted_numbers[position]:
            return position
        if sorted_numbers[position] < integer:
            return interpolationSearch(sorted_numbers, integer, position + 1, high)
        if sorted_numbers[position] > integer:
            return interpolationSearch(sorted_numbers, integer, low, position - 1)
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
    index = interpolationSearch(rand_array, element, 0, limit-1)
    if index != -1:
        print(f"{element} found at index {index} in the sorted array.")
    else:
        print(f"{element} is not in the array.")
