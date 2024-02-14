#  Insertion sort is not fast sorting algorithm because it uses nested loops to sort
# It is useful for small data sets
# It runs in O(n^2).


def  insertion_sort(A):
    for i in range(1, len(A)):
        j = i
        while A[j - 1] > A[j] and j > 0:
            A[j - 1], A[j] = A[j] , A[j - 1]
            j -= 1


arr = [8, 5, 1, 10, 75, 0, 2, 3]
insertion_sort(arr)
print(arr)

