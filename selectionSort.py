def selectionSort(A):
     for i in range(len(A)): #compare A[i] element with Remaining elements
          smallest = findSmall(A,i) # Find the smallest one from ith element
          swap(i,smallest,A) # replace with ith element
def findSmall(A,i): # find the smallest number from ith element
     small = i
     for f in range(i+1,len(A)):
          if A[small] > A[f]:
               small = f
     return small
def swap(ini,small,A): # Swap the A[ini] with A[small] element
     helper = A[ini]
     A[ini] = A[small]
     A[small] = helper

array = [4,3,5,0,1,6,7,9,10]
selectionSort(array)
print(array)
