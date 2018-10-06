def selectionSort(A):
     for i in range(len(A)):
          smallest = findSmall(A,i)
          swap(i,smallest,A)


def findSmall(A,i):
     small = i
     for f in range(i+1,len(A)):
          if A[small] > A[f]:
               small = f
     return small

def swap(ini,small,A):
     helper = A[ini]
     A[ini] = A[small]
     A[small] = helper

array = [4,3,5,0,1,6,7,9,10]
selectionSort(array)
print(array)
