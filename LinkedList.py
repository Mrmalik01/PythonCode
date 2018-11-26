class Node: 
    def __init__(self,data,next):
        self.data = data
        self.next = next
    def __str__(self):
        return str(data)

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.total = 0
    
    def size(self):
        return self.total
    
    def get(self,i):
        if self.head == None:
            return None
        else:
            ptr = self.head
            while i>0 and ptr != None:
                ptr = ptr.next
                i-=1
            return ptr.data
    
    def append(self,data):
        if self.head == None:
            self.head = Node(data,None)
        else:
            ptr = self.head
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = Node(data,None)
        self.total+=1
        
    def remove(self,data):
        if self.head == None:
            return 
        elif self.head.data == data:
            self.head = self.head.next
            self.total-=1
        else:
            ptr = self.head
            while ptr.next != None:
                if ptr.next.data == data:
                    ptr.next = ptr.next.next
                    self.total-=1
                ptr = ptr.next
    
    def insert(self,i,data):
        if self.head == None or i == 0:
            self.head = Node(data,self.head)
        else:
            ptr = self.head
            while i>1 and ptr != None:
                ptr = ptr.next
                i-=1
            ptr.next = Node(data,ptr.next)
        self.total+=1
    
    def print(self):
        res = "["
        ptr = self.head
        while ptr != None:
            if ptr.next == None:
                res+=str(ptr.data)
                break
            res+= str(ptr.data)+","
            ptr = ptr.next
        print(res+"]")