def insertionSort(A):
     # compare A[i] with all A[0]...A[i] elements
     for i in range(1,len(A)):
          insert(A[i],i,A)
          
def insert(k,hi,A):
     # compare k with all A[0]...A[i]
     for i in range(hi,0,-1):
          # if k is greater or equals to A[i-1], then assign A[i] to k
          if k >= A[i-1]:
               # if k is greater than the last element then insert k in empty or copied position (A[i])
               A[i] = k
               return
          # else move A[i-1] element to one index ahead, such that A[i-1] is empty or copy of A[i]
          A[i]= A[i-1]
     A[0] = k



array = [4,3,5,0,1,6,7,9,10]
insertionSort(array)
print(array)

