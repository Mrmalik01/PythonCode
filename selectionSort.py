def selectionSort(A):
     #compare A[i] element with Remaining elements 
     for i in range(len(A)):
          smallest = findSmall(A,i) # Find the smallest one from ith element
          swap(i,smallest,A) # replace with ith element

# find the smallest number from ith element
def findSmall(A,i):
     small = i
     for f in range(i+1,len(A)):
          if A[small] > A[f]:
               small = f
     return small

# Swap the A[ini] with A[small] element
def swap(ini,small,A):
     helper = A[ini]
     A[ini] = A[small]
     A[small] = helper

array = [4,3,5,0,1,6,7,9,10]
selectionSort(array)
print(array)
