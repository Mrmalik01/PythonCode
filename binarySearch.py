def search(A,k):
     lo = 0
     hi = len(A)
     while lo<= hi:
          mid = (lo+hi)//2
          if A[mid] == k:
               return mid
          else:
               if A[mid] < k:
                    lo = mid+1
               else:
                    hi = mid-1
     return -1;

print(search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],12))
