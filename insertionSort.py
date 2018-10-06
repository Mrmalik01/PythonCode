import time
def insertionSort(A):
     for i in range(1,len(A)): # compare A[i] with all A[0]...A[i] elements
          insert(A[i],i,A) 
def insert(k,hi,A):    
     for i in range(hi,0,-1): # compare k with all A[0]...A[i]
          if k >= A[i-1]: # if k is greater or equals to A[i-1], then assign A[i] to k
               A[i] = k # if k is greater than the last element then insert k in empty or copied position (A[i])
               return
          A[i]= A[i-1] # else move A[i-1] element to one index ahead, such that A[i-1] is empty or copy of A[i]
     A[0] = k
     
def algorithmTester(f,A):
     t = time.time()*1000
     sorted = f(A)
     t = time.time()*1000-t
     print("This algorithms took "+str(t)+" miliseconds")
     print(sorted)
     
array = [4,3,5,0,1,6,7,9,10]
insertionSort(array)
print(array)
algorithmTester(insertionSort,array)

