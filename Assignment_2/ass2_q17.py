# Bubble Sort function
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]

# List of integers
arr = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]

# Sorting the list using bubble sort
bubble_sort(arr)

# Printing the sorted list
print("Sorted list:", arr)
