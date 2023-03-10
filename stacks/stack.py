'''Stacks - LIFO Data Structure:- the most recently added object is the first to be removed
- Everything works on the top of the stack
- Time Complexity:-
- Access: O(n)
- Search: O(n)
- Insert: O(1)
- Remove: O(1)
- '''

'''Implementation of stack using lists in python'''

class Stack:
    def __init__(self):
        self.data = []
    
    # push method that stores the value in a stack
    def push(self, val):
        self.data.append(val)
    
    def pop(self):
        top = self.data.pop()
        return top
    
    def peek(self):
        return self.data[len(self.data) - 1]
    
    def nextToTop(self):
        return self.data[-2]
    
    def clear(self):
        self.data.clear()
    
    def isEmpty(self):
        if (len(self.data)):
            return False
        
        return True
    
    def search(self, val):
        #linear search
        for i in range(len(self.data)):
            if (self.data[i] == val):
                print("Found ")
                return i
            
        else:
            print("Not found")
            return -1
    
def main():
    myStack = Stack()
    print(myStack.isEmpty())
    myStack.push(1)
    myStack.push(5)
    myStack.push(3)
    topVal = myStack.pop()
    print(topVal)
    
    print(myStack.isEmpty())
    myStack.push(8)
    print(myStack.search(5))
    
     
if __name__ == "__main__":
    main()
        
    
            
        
    
    
            
