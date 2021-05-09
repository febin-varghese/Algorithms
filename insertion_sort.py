# Insertion sort algorithm to sort a set of random numbers
import numpy as np


def insertionSort(numbers):
    for j in range(len(numbers)):
        if j == 0:
            continue
        k = j
        while numbers[k] < numbers[k-1] and k > 0:
            numbers[k - 1], numbers[k] = numbers[k], numbers[k - 1]
            k -= 1
        # for k in range(j, 0, -1):
        #     if numbers[k] < numbers[k-1]:
        #         numbers[k-1], numbers[k] = numbers[k], numbers[k-1]
        #     else:
        #         break


if __name__ == "__main__":
    limit = 10
    rand_array = np.random.randint(0, 100, limit)
    print("numbers")
    print(rand_array)
    insertionSort(rand_array)
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
