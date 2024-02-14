# Divide and conquer algorithm
# Breaks down problem into multiple subproblems recursively until they become simple to solve
# Solutions are compined to solve original problem
# O(n * log(n)) running time -> Optimal running time for comparison based algorithms
#  Merge Sort principle :
#      1) Split array in half
#      2) Call merge sort on each half to sort them recursively
#      3) Merge both sorted haves into one sorted array


def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr) // 2]
        right_arr = arr[len(arr) // 2:]
        
        # recursion
        merge_sort(left_arr)
        merge_sort(right_arr)
        
        # merge
        i = 0  # left arr index
        j = 0  # right arr index
        k = 0  # merged arr index

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
            
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


arr_test = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]
merge_sort(arr_test)
print(arr_test)
