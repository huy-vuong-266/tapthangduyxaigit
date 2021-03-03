class Stack:
    def __init__(self):
        self.stack = []

    def put(self,data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty() == True:
            return "Stack out of range"
        else:
            a = self.stack[len(self.stack)-1]
            self.stack.pop()
            return a
    
    def size(self):
        return len(self.stack)

    def front(self):
        return self.stack[0]

    def back(self):
        return self.stack[-1]

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False

    def getStack(self):
        return self.stack
