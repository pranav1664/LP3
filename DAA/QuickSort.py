import random
import time

def deterministic_quicksort(alist, start, end):
    '''Deterministic quicksort using the first element as pivot.'''
    if end - start > 1:
        p = deterministic_partition(alist, start, end)
        deterministic_quicksort(alist, start, p)
        deterministic_quicksort(alist, p + 1, end)

def deterministic_partition(alist, start, end):
    pivot = alist[start]
    i = start + 1
    j = end - 1

    while True:
        while (i <= j and alist[i] <= pivot):
            i += 1
        while (i <= j and alist[j] >= pivot):
            j -= 1

        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j

def randomized_quicksort(alist, start, end):
    '''Randomized quicksort using a random pivot.'''
    if end - start > 1:
        p = randomized_partition(alist, start, end)
        randomized_quicksort(alist, start, p)
        randomized_quicksort(alist, p + 1, end)

def randomized_partition(alist, start, end):
    random_index = random.randint(start, end - 1)
    alist[start], alist[random_index] = alist[random_index], alist[start]
    return deterministic_partition(alist, start, end)

try:
    size = int(input('Enter the number of random numbers to generate: '))
    if size <= 0:
        raise ValueError("Size must be a positive integer.")

    alist_deterministic = [random.randint(0, 10000) for _ in range(size)]
    alist_randomized = alist_deterministic.copy()  # Copy for randomized sort

    print('Unsorted list:', alist_deterministic)

    # Time deterministic quicksort
    start_time = time.time()
    deterministic_quicksort(alist_deterministic, 0, len(alist_deterministic))
    end_time = time.time()
    print('Sorted list (Deterministic):', alist_deterministic)
    deter_time = end_time - start_time

    # Time randomized quicksort
    start_time = time.time()
    randomized_quicksort(alist_randomized, 0, len(alist_randomized))
    end_time = time.time()
    print('Sorted list (Randomized):', alist_randomized)
    print(f'Time taken for randomized sort: {end_time - start_time:.6f} seconds')
    print(f'Time taken for deterministic sort: {deter_time:.6f} seconds')

except ValueError as e:
    print(f'Invalid input: {e}')
