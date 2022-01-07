def binarysearch(A, key):
    low = 0
    high = len(A)-1
    while low <= high:
        mid =(low + high) // 2
        if key == A[mid] :
            return True
        elif key < A[mid]:
            high = mid - 1
        else :
            low = mid + 1
    return False

A = [15,21,47,84,96]
found = binarysearch(A,96)
print('The Element 96: ',found)
