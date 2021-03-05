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
        openlist = []
        closelist =[]
        openlist.append(s)
        np = {} #luu node di qua
        np[s] = 0
        gCost = {}
        fCost = {}
        gCost[s] = 0
        fCost[s] = gCost[s] + h[s][0]
        cpwh = []#cost path without heuristic
        while len(openlist) != 0:
            currentNode = self.getLowestNode(openlist,fCost)
            if currentNode == g:
                #return self.reconstructPath(np,g)
                return cpwh[-1]
            openlist.remove(currentNode)
            closelist.append(currentNode)
            for (i,v) in self.graph[currentNode]:
                tc = gCost[currentNode] + v
                if i not in closelist and i not in openlist:
                    np[i] = currentNode
                    gCost[i] = tc
                    fCost[i] = gCost[i] + h[i][0]
                    cpwh.append(tc)
                    openlist.append(i)
                else:
                    if i in closelist:
                        continue
        return 0
        #code tham khao tu` https://github.com/vandersonmr/A_Star_Algorithm/blob/master/libs/python/AStar.py
        pass
    def getLowestNode(self,open_list,h):
        minHeuristic = h[open_list[0]]
        lowestNode = None
        for n in open_list:
            if h[n] <= minHeuristic:
                minHeuristic = h[n]
                lowestNode = n
        return lowestNode
    
    def reconstructPath(self,cameFrom,goal):
        path = []
        Node = goal
        path.appendleft(Node)
        while n in cameFrom:
            Node = cameFrom[Node]
            path.appendleft(Node)
        return

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

print(g.A_star(start, goal, heuristic))
f = open("output.txt", "w")
f.write(str(g.A_star(start, goal, heuristic)))