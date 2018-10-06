import random,time
def arrayGenerator(n):
     array = []
     for i in range(n):
          array.append(random.randint(0,n))
     return array

def algorithmTester(f,A):
     t = time.time()*1000
     sorted = f(A)
     t = time.time()*1000-t
     print("This algorithms took "+str(t)+" miliseconds")
     print(sorted)
     
