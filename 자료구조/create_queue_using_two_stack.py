class Stack:
    def __init__(self):
        self.st = []
        self.max = 10
        
    def push(self, data):
        self.st.append(data)
        
    def pop(self):
        return self.st.pop()
    
    def print(self):
        print(self.st)
        
    def peek(self):
        return self.st[-1]
    
    def isEmpty(self):
        if len(self.st) == 0:
            return True
        return False
    
    def size(self):
        return len(self.st)
    
    
class Queue:
    def __init__(self):
        self.st1 = Stack()
        self.st2 = Stack()
        
    def enqueue(self, data):
        self.st1.push(data)
        
    def dequeue(self):
        if self.st2.isEmpty():
            while self.st1.isEmpty() == False:
                self.st2.push(self.st1.pop())
    
        return self.st2.pop()
    
    
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    
    print(q.dequeue())
    q.enqueue(3)
    print(q.dequeue())
    
