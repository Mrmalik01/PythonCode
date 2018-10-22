# Author : Khizar Malik
# Date : 22 Oct 2018
def quickSort(A):
     quickSortRec(A,0,len(A))

def quickSortRec(A,lo,hi):
     if hi-lo <=1:
          return
     iPivot = partition(A,lo,hi)
     quickSortRec(A,lo,iPivot)
     quickSortRec(A,iPivot+1,hi)

def partition(A,lo,hi):
     pivot = A[lo]
     B = [0 for i in range(lo,hi)]
     loB = 0
     hiB = len(B)-1
     for i in range(lo+1,hi):
          if A[i]<pivot:
               B[loB] = A[i]
               loB+=1
          else:
               B[hiB] = A[i]
               hiB+=1
     B[loB] = pivot
     for i in range(lo,hi):
          A[i] = B[i-lo]
     return loB+lo

A = [10,9,8,7,6,5,4,3,2,1]
quickSort(A)
print(A)
