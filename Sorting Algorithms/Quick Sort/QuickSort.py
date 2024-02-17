# Divide and conquer algorithm
# Breaks down problem into multiple subproblems recursively until they become simple to solve
# Solutions are compined to solve original problem
# O(n^2) running time -> worst case
# O(n * log(n)) running time -> best and average case

# Quick sort principle:
#  1) Choose pivot element usually (last or random)
#  2) Stores elements les than pivot in left subarray
#     and stores elements greater than pivot in right subarray
#  3) Call quick sort recursively on left subarray
#     Call quick sort recursively on right subarray


def quickSort(arr, left, right):
    if left < right:
        partion_pos = partion(arr, left, right)
        quickSort(arr, left, partion_pos - 1)
        quickSort(arr, partion_pos + 1, right)

        
def partion(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]
    
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left  and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
        
    return i;


arr = [22, 11, 88, 66, 55, 77, 33, 4]
quickSort(arr, 0, len(arr) - 1)
print(arr)
