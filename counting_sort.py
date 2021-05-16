# Counting sort algorithm to sort a set of random numbers
# best for numbers in a small range

import numpy as np


def countingSort(numbers):
    countingArray = np.zeros(100)
    for n in numbers:
        countingArray[n] += 1
    for idx in range(1, len(countingArray)):
        countingArray[idx] = countingArray[idx-1] + countingArray[idx]
    sortedArray = np.empty_like(numbers)
    for n in numbers:
        outArrayIdx = int(countingArray[n] - 1)
        sortedArray[outArrayIdx] = n
        countingArray[n] -= 1
    return sortedArray


if __name__ == "__main__":
    # Random number generation
    limit = 10
    rand_array = np.random.randint(0, 100, limit)
    print("numbers")
    print(rand_array)
    # sort
    rand_array = countingSort(rand_array)
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
