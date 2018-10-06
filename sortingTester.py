import random,time
def arrayGenerator(n):
     array = []
     for i in range(n):
          array.append(random.randint(0,n))
     return array

def algorithmTester(t,A):
     t = time.time()*1000
     sorted = t(A)
     t = time.time()*1000-t
     print("This algorithms took "+t+" miliseconds")
     print(sorted)
     
