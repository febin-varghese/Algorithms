# Bottom up merge sort algorithm to sort a set of random numbers
import numpy as np
import copy


def merge(numbers, start, middle, end):
    """
    Merging
    :param numbers: Numpy array of random numbers
    :param start:
    :param middle:
    :param end:
    :return: None
    """
    sz = end - start
    temp_array = np.zeros(sz)
    i1 = copy.deepcopy(start)
    j = copy.deepcopy(middle)
    k = 0
    while i1 < middle or j < end:
        if i1 < middle and j < end:
            if numbers[i1] < numbers[j]:
                temp_array[k] = numbers[i1]
                k += 1
                i1 += 1
            else:
                temp_array[k] = numbers[j]
                k += 1
                j += 1
        elif i1 == middle:
            temp_array[k] = numbers[j]
            k += 1
            j += 1
        elif j == end:
            temp_array[k] = numbers[i1]
            k += 1
            i1 += 1

    for i1 in range(start, end):
        numbers[i1] = temp_array[i1 - start]


def mergeSort(numbers):
    """
    Merge sort
    :param numbers: Numpy array of random numbers
    :return: None
    """
    width = 1
    while width < len(numbers):
        for idx in range(0, len(rand_array), 2 * width):
            start = idx
            middle = min(idx + width, len(rand_array))
            end = min(idx + (2 * width), len(rand_array))
            merge(numbers, start, middle, end)
        width = width * 2


if __name__ == "__main__":
    limit = 10
    rand_array = np.random.randint(0, 100, limit)
    print("numbers")
    print(rand_array)
    mergeSort(rand_array)
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
