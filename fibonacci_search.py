# Fibonacci search algorithm
# Uses quick sort for sorting

import numpy as np
from quick_sort import quickSort


def fibonacciSearch(sorted_numbers, integer):
    length = len(sorted_numbers)
    fibonacci_numbers =[0, 1]
    k = 1
    m = 1
    while m < length:
        m = fibonacci_numbers[k] + fibonacci_numbers[k - 1]
        fibonacci_numbers.append(m)
        k += 1
    if m == 0:
        return -1
    offset = -1
    while m > 1:
        idx = min(offset + fibonacci_numbers[k-2], length - 1)
        if sorted_numbers[idx] == integer:
            return idx
        elif integer > sorted_numbers[idx]:
            k -= 1
            m = fibonacci_numbers[k]
            offset = idx
        else:
            k -= 2
            m = fibonacci_numbers[k]
    return -1


if __name__ == "__main__":
    # Random number generation
    print("Fibonacci search algorithm")
    limit = 100
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
