'''Queue data structure - FIFO
A Queue is a collection of elements, supporting two principle operations: 
enqueue, which inserts an element into the queue, and dequeue, which removes 
an element from the queue
First in, first out data structure (FIFO): the oldest added object is the first to be removed
Time Complexity:
Access: O(n)
Search: O(n)
Insert: O(1)
Remove: O(1)'''

'''implementation of a queue using deque'''

from collections import deque

class Queue:
    def __init__(self):
        self.data = deque() # using the imported deque
        
    # we are entering the values from the left side
    def enqueue(self, val):
        self.data.appendleft(val)
    
    # we are removing the values from the right side
    def dequeue(self):
        self.data.pop()
    
    def isEmpty(self):
        return len(self.data) == 0
    
    def size(self):
        return len(self.data)

def main():
    my_queue = Queue()
    my_queue.enqueue(5)
    my_queue.enqueue(10)
    my_queue.enqueue(15)
    my_queue.enqueue(20)
    print(my_queue.size())
    print(my_queue.data)
    my_queue.dequeue()
    print(my_queue.data)
    
if __name__ == "__main__":
    main()
    
    