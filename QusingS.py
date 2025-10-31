# we use two stacks. if enqueue, directly push into stack 1. if dequeue, copy into second stack s2 in reversed order then pop from s2.
# for peek, same dequeue just return element instead of pop. 

class myQueue:
    def __init__(self):
        # Two stacks for implementing queue
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        # Always push new elements into s1
        self.s1.append(x)

    def dequeue(self):
        # If both stacks are empty → queue is empty
        if not self.s1 and not self.s2:
            return -1

        # If s2 is empty, move all elements from s1 to s2
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        # Remove and return the front element
        return self.s2.pop()

    def front(self):
        # If both stacks are empty → no front
        if not self.s1 and not self.s2:
            return -1

        # Move elements to s2 if needed
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        # Return the front element
        return self.s2[-1]

    def size(self):
        # Total number of elements
        return len(self.s1) + len(self.s2)
