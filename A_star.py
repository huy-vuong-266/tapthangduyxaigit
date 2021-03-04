from collections import defaultdict
from utils import *
import heapq

# define graph
class Graph:

    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v, l):
        self.graph[u].append((v, l))

    # function to be implemented
    def A_star(self, s, g, h):
        pq = PriorityQueue()
        visited = []
        visited.append(s)
        cl =[]
        sh = 0
        for v, w in self.graph[s]:
           pq.update(item=v, priority=h[v][0] + w)
           cl.append((s,v))
           
        while not pq.isEmpty():
            (pri, it) = pq.pop()

            if it == g:
                visited.append(it)
                break
            visited.append(it)
            for v,w in self.graph[it]:
                if  v not in visited:
                    cl.append((it,v))
                    pq.update(item=v, priority=h[v][0]+pri+w)
        # th = self.traceBack(s,g,cl)
        # print(th)
        # for f  in range(len(th)):
        #        sh = sh + h[th[f]][0]
        print(visited)
        pass

    # def traceBack(self,s,g,cl):
    #     GBFSlist = []
    #     f,t = cl.pop(-1)
    #     GBFSlist.append(t)
    #     GBFSlist.append(f)
    #     while f != s:
    #         f = self.findPreviousNode(f,cl)
    #         GBFSlist.append(f)
    #     return GBFSlist    
            
    # def findPreviousNode(self,node,cl):
    #     f,t = cl.pop(-1)
    #     while t != node:
    #         f,t = cl.pop(-1)
    #     return f    
        
    

# Driver code
# Create a graph given in the above diagram
g = Graph()
heuristic = []

with open('input.txt', 'r') as f:
    n, m = [int(x) for x in next(f).split()]
    for i in range(m):
        u, v, l = [int(x) for x in next(f).split()]
        g.addEdge(u, v, l)
    for i in range(n):
        h = [int(x) for x in next(f).split()]
        heuristic.append(h)
    start, goal = [int(x) for x in next(f).split()]

g.A_star(start, goal, heuristic)