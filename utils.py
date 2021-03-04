import heapq

class PriorityQueue:
    """
      Implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.
    """
    def  __init__(self):
        self.pq = []
        pass

    def push(self, item, priority):
        heapq.heappush(self.pq,(priority,item))
        heapq.heapify(self.pq)
        pass
    
    def get(self,item,priority):
        return self.pq(priority,item)

    def pop(self):
        if (len(self.pq)==0):
            return
        res = heapq.heappop(self.pq)
        heapq.heapify(self.pq)
        return res
        pass

    def isEmpty(self):
        if len(self.pq) == 0:
            return True
        return False

        pass

    def update(self, item, priority):
        # If item already in priority queue with higher priority, update its priority and rebuild the heap.
        # If item already in priority queue with equal or lower priority, do nothing.
        # If item not in priority queue, do the same thing as self.push.
        exist = False
        for p, i in self.pq:
            if item == i:
                exist = True
                if p > priority:
                    self.pq.remove((p,i))
                    self.push(item,priority)
                    break
        if exist == False:
            self.push(item,priority)
        pass