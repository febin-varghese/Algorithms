# Bubble sort algorithm to sort a set of random numbers
import numpy as np


def bubbleSort(numbers):
    for j in range(len(numbers)):
        for k in range(j+1, len(numbers)):
            if numbers[k] < numbers[j]:
                numbers[j], numbers[k] = numbers[k], numbers[j]


if __name__ == "__main__":
    limit = 10
    rand_array = np.random.randint(0, 100, limit)
    print("numbers")
    print(rand_array)
    bubbleSort(rand_array)
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
