def linearsearch(A, key):
    position = 0
    flag = 0
    while position < len(A) and not flag:
        if A[position] == key :
            flag = True
        else :
            position = position + 1
    return flag

A = [3, 5, 7, 9, 32, 45]
found = linearsearch(A, 9)
print('Element 9 is present : ',found)