"""Binary search in an  array."""


def binarysearch(A, start, end, x):
    """Finding an element in an arrary."""
    while (start <= end):
        mid = (start+end)//2
        if A[mid] == x:
            return mid
        elif x < A[mid]:
            mid = mid-1
            return binarysearch(A, start, mid, x)
        else:
            return binarysearch(A, mid+1, end, x)


array = [2, 3, 4, 10, 40, 60]
x = 60
length = len(array)
start = 0
end = length - 1
result = binarysearch(array, start, end, x)
print(result)
