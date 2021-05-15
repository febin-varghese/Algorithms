# Bucket sort algorithm to sort a set of random numbers
# best for uniformly distributed numbers

import numpy as np

# user defined imports
from insertion_sort import insertionSort


def bucketSort(numbers):
    length = len(numbers)
    buckets = [[] for _ in range(length)]
    for n in numbers:
        buckets[n // length].append(n)
    for b in buckets:
        if b:
            insertionSort(b)
    numbers = np.array([num for bucket in buckets for num in bucket])
    return numbers


if __name__ == "__main__":
    # Random number generation
    limit = 10
    rand_array = np.random.randint(0, 100, limit)
    print("numbers")
    print(rand_array)
    # sort
    rand_array = bucketSort(rand_array)
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
