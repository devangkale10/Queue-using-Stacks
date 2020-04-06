class Node :
    def __init__(self,value) :
        self.value=value
        self.next=None

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.top=None
        self.bottom=None
        self.length=0
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if(self.length==0) :
            newNode = Node(x)
            self.top=newNode
            self.bottom=newNode
            self.length+=1
        else:
            newNode = Node(x)
            self.bottom.next=newNode
            self.bottom=newNode
            self.length+=1
                
        
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if(self.length==0):
            return None
        
        holdingPointer=self.top.value
        self.top=self.top.next
        self.length-=1
        return holdingPointer
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if(self.length==0):
            return None
        else:
            holdingPointer=self.top.value
            return holdingPointer
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if(self.length==0):
            return True
        return False
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()