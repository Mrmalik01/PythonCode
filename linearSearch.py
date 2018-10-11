def linearSearch(A,k):
    for i in range(len(A)):
        if A[i] >= k:
            break
    if A != [] and A[i] == k :
        return i
    return -1


    
