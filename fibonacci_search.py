# Fibonacci search algorithm
# Uses quick sort for sorting

import numpy as np
from quick_sort import quickSort


def fibonacciSearch(sorted_numbers, integer):
    length = len(sorted_numbers)
    m2 = 0
    m1 = 1
    m = m1 + m2
    while m < length:
        m2 = m1
        m1 = m
        m = m1 + m2
    offset = -1
    while m > 1:
        idx = min(offset + m2, length-1)
        if sorted_numbers[idx] < integer:
            m = m1
            m1 = m2
            m2 = m - m1
            offset = idx
        elif sorted_numbers[idx] > integer:
            m = m2
            m1 = m1 - m2
            m2 = m - m1
        else:
            return idx
    if m1 and sorted_numbers[length-1] == integer:
        return length - 1
    return -1


if __name__ == "__main__":
    # Random number generation
    print("Fibonacci search algorithm")
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
    index = fibonacciSearch(rand_array, element)
    if index != -1:
        print(f"{element} found at index {index} in the sorted array.")
    else:
        print(f"{element} is not in the array.")
