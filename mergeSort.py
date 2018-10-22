# Author : Khizar Malik
# Date : 22 Oct 2018

def mergeSort(A):
     if len(A) <=1:
          return
     mid = len(A)//2
     half1 = A[:mid]
     half2 = A[mid:]
     mergeSort(half1)
     mergeSort(half2)
     merge(half1,half2,A)

def merge(h1,h2,A):
     i = 0; j1 = 0; j2 = 0
     while j1 <len(h1) and j2 <len(h2):
          if h1[j1]<h2[j2]:
               A[i] = h1[j1]
               j1+=1; i+=1
          else:
               A[i] = h2[j2]
               j2+=1; i+=1
     while j1 < len(h1):
          A[i] = h1[j1]
          j1+=1; i+=1
     while j2 < len(h2):
          A[i] = h2[j2]
          j2+=1; i+=1


A = [10,9,8,7,6,5,4,3,2,1]
mergeSort(A)
print(A)
