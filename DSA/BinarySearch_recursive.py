def binarysearch_R(A, key, low, high):
    if low > high :
        return False
    else :
        mid = (low + high) // 2
        if key == A[mid]:
            return True
        elif key < A[mid] :
            return binarysearch_R(A, key, low, mid-1)
        else:
            return binarysearch_R(A, key, mid+1, high)

A = [15,21,47,84,96]
found = binarysearch_R(A,84,0,5)
print('The Element 84: ', found)