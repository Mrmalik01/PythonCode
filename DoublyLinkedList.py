class Node:
    def __init__(self,data,next,prev):
        self.data = data
        self.next = next
        self.prev = prev
        
    def __str__(self):
        return str(self.data)

class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.total = 0
        
    def get(self,i):
        if self.head == None:
            return None
        ptr = self.head
        while i>0 and ptr != None:
            ptr = ptr.next
            i-=1
        return ptr.data
    
    def size(self):
        return self.total
        
    def append(self,data):
        if self.head == None and self.tail == None:
            self.head = Node(data,None,None)
            self.tail = self.head
        else:
            self.tail.next = Node(data,None,self.tail)
            self.tail = self.tail.next
        self.total+=1
        
    def remove(self,data):
        if self.head == None:
            return
        elif self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            self.total -=1
        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            self.total -=1
        else:
            ptr = self.head
            while ptr.next != None:
                if ptr.next.data == data:
                    ptr.next = ptr.next.next
                    ptr.next.prev = ptr
                    self.total -=1
                ptr = ptr.next
        
    def insert(self,i,data):
        if self.head == None:
            self.head = Node(data,None,None)
            self.tail = self.head
        elif i == 0:
            self.head.prev = Node(data,self.head,None)
            self.head = self.head.prev
        elif i == self.total:
            self.tail.next = None(data,None,self.tail)
            self.tail = self.tail.next
        else:
            ptr = self.head
            while i>1 and ptr != None:
                ptr = ptr.next
                i-=1
            ptr.next = Node(data,ptr.next,ptr)
            ptr.next.next.prev = ptr.next
        self.total+=1
        
    def print(self):
        ptr = self.head
        res = "["
        while ptr != None:
            if ptr.next == None:
                res+=str(ptr)
                break
            res+=str(ptr)+","
            ptr = ptr.next
        print(res+"]")