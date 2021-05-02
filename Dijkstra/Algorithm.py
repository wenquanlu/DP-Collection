import sys
import heapq

# Adjacency List representation of graph
class edge:
    def __init__(self, name):
        self.name = name
        self.left_node = None   #connects to vertice object 
        self.right_node = None  #connects to vertice object 
        self.next = None    #next edge object 
        self.length = None

class incident_edges:
    def __init__(self):
        self.next = None        #next incident edge
        self.actual_edge = None #the actual edge it points to 


class vertice:
    def __init__(self, name):
        self.name = name    
        self.incident_edges = None  #list of incident edges
        self.next = None        #next vertice 
        self.distance = sys.maxsize
        self.parent = None
    def __lt__(self, other):
        return self.distance > other.distance


def Dijkstra(start):
    start.distance = 0
    node = start
    q = []
    while node != None:
        heapq.heappush(q, node)
        node = node.next
    while len(q) != 0:
        u = heapq.heappop(q)
        x = u.incident_edges
        while x != None:
            z = None
            if x.actual_edge.left_node == u:
                z = x.actual_edge.right_node
            else:
                z = x.actual_edge.left_node
            if u.distance + x.actual_edge.length < z.distance:
                z.distance = u.distance + x.actual_edge.length
                heapq.heappush(q, z)
                z.parent = u
            x = x.next
