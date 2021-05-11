# Heap sort algorithm to sort a set of random numbers
# 1. Heapify the binary tree
# 2. Heap sort
# Reference https://www.geeksforgeeks.org/building-heap-from-array/
import numpy as np


def heapifyArray(numbers, length, root_idx):  # there exists a "heapify" function in Python
    largest_node_idx = root_idx
    left_child_idx = 2 * root_idx + 1
    right_child_idx = 2 * root_idx + 2
    if left_child_idx < length and numbers[left_child_idx] > numbers[largest_node_idx]:
        largest_node_idx = left_child_idx
    if right_child_idx < length and numbers[right_child_idx] > numbers[largest_node_idx]:
        largest_node_idx = right_child_idx
    if largest_node_idx != root_idx:
        numbers[root_idx], numbers[largest_node_idx] = numbers[largest_node_idx], numbers[root_idx]
        heapifyArray(numbers, length, largest_node_idx)


def buildHeap(numbers):
    # last non-leaf (lnl) node = (n/2) -1; n = total number of nodes = length of array
    # heapify nodes [0 to lnl] in the reverse order
    length = len(numbers)
    start_idx = length // 2 - 1  # // integer division
    for idx in range(start_idx, -1, -1):
        heapifyArray(numbers, length, idx)


def heapSort(numbers):
    for idx in range(len(numbers)-1, 0, -1):
        numbers[idx], numbers[0] = numbers[0], numbers[idx]
        heapifyArray(numbers, idx, 0)


if __name__ == "__main__":
    # Random number generation
    limit = 11
    rand_array = np.random.randint(0, 100, limit)
    print("numbers")
    print(rand_array)
    # build heap
    buildHeap(rand_array)
    # sort
    heapSort(rand_array)
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
