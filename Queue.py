class Queue:
    def __init__(self):
        super().__init__()
        self.queue = []
    
    def enQueue(self,data):
        self.queue.append(data)

    def deQueue(self):
        if self.is_empty() == True:
            return "Queue out of range"
        else:
            a = self.queue[0]
            self.queue.pop(0)
            return a
    
    def size(self):
        return len(self.queue)

    def front(self):
        return self.queue[0]

    def back(self):
        return self.queue[len(self.queue)-1]
    
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        return False

    def getQueue(self):
        return self.queue