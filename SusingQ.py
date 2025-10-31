# implementing stack using queue
# if enqueue, push new element and make it the top by rotating
# if dequeue, just popleft() from queue


from collections import deque


class myStack:

    def __init__(self):
        self.q = deque()

    def push(self, x):
        # push element on top
        self.q.append(x)
        
        for j in range(len(self.q)-1):
            self.q.append(self.q.popleft())
        
        
    def pop(self):
        # remove top element
        if not self.q:
            return
        else:
            self.q.popleft()
        
    def top(self):
        # return top element
        if not self.q:
            return -1
        else:
            return self.q[0]
        
    def size(self):
        # return current size
        return len(self.q)
        
