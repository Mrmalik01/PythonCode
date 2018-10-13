# Author : Khizar Malik
# Date : 13 Oct 2018
# This is version of Insertion Sort in which it add sorted element in the new array without making any change in original array
def insertionSortConst(A):
    newArray = [0 for i in range(len(A))]
    newArray[0] = A[0]
    for i in range(1,len(A)):
        insert(A,A[i],i,newArray)
    return newArray

def insert(A,elem,index,B):
    for i in range(index,0,-1):
        if B[i-1]<=elem:
            B[i] = elem
            return
        B[i] = B[i-1]
    B[0] = elem


print(insertionSortConst([10,9,8,7,6,5,4,3,2,1]))
# Output : 1,2,3,4,5,6,7,8,9,10
