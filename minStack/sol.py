'''

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2


Constraints:

Methods pop, top and getMin operations will always be called on non-empty stacks.

'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = Stack()
        self.minStack = Stack()

    def push(self, x: int) -> None:
        self.stack.push(x)
        if self.minStack.length() == 0 or self.minStack.top() >= x:
          self.minStack.push(x)

    def pop(self) -> None:
      if self.stack.length() > 0:
        lastItem = self.stack.pop()
        if lastItem == self.minStack.top():
          self.minStack.pop()

    def top(self) -> int:
      if self.stack.length() > 0:
        return self.stack.top()

    def getMin(self) -> int:
      if self.minStack.length() > 0:
        return self.minStack.top()


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class Stack:
  def __init__(self):
    self.storage = {}
    self.size = 0
  
  def push(self, val):
    self.storage[self.size] = val
    self.size += 1

  def pop(self):
    top = self.storage[self.size - 1]
    del self.storage[self.size - 1]
    self.size -= 1
    return top
  
  def top(self):
    return self.storage[self.size - 1]

  def length(self):
    return self.size