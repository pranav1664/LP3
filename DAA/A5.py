# Write a program for analysis of quick sort by using deterministic and randomized variant.

import random
import time

def partition_deterministic(arr, low, high):
    pivot = arr[high] 
    i = low - 1  
    swap_count = 0  
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] 
            swap_count += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  
    swap_count += 1
    return i + 1, swap_count

def quicksort_deterministic(arr, low, high):
    swap_count = 0
    if low < high:
        pi, swaps = partition_deterministic(arr, low, high)
        swap_count += swaps
        swap_count += quicksort_deterministic(arr, low, pi - 1)
        swap_count += quicksort_deterministic(arr, pi + 1, high)
    return swap_count

def partition_randomized(arr, low, high):
    pivot_index = random.randint(low, high) 
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  
    return partition_deterministic(arr, low, high)  

def quicksort_randomized(arr, low, high):
    swap_count = 0
    if low < high:
        pi, swaps = partition_randomized(arr, low, high)
        swap_count += swaps
        swap_count += quicksort_randomized(arr, low, pi - 1)
        swap_count += quicksort_randomized(arr, pi + 1, high)
    return swap_count

def main():
    n = int(input("Enter the number of elements in the array: "))
    arr = [random.randint(0, 1000) for _ in range(n)] 

    arr_deterministic = arr.copy()
    arr_randomized = arr.copy()

    print("\nDeterministic QuickSort:")
    start_time = time.time()
    swaps_deterministic = quicksort_deterministic(arr_deterministic, 0, n - 1)
    end_time = time.time()
    print(f"Sorted Array: {arr_deterministic}")
    print(f"Number of swaps: {swaps_deterministic}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")

    print("\nRandomized QuickSort:")
    start_time = time.time()
    swaps_randomized = quicksort_randomized(arr_randomized, 0, n - 1)
    end_time = time.time()
    print(f"Sorted Array: {arr_randomized}")
    print(f"Number of swaps: {swaps_randomized}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    main()
