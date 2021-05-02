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


"""
adjacency matrix representation of the graph
  a  b  c  d  e  f
a 0  u1 0  v5 0  l7
b u1 0  w3 0  x9 0
c 0  w3 0  y2 0  z4
d v5 0  y2 0  m6 0
e 0  x9 0  m6 0  n8
f l7 0  z4 0  n8 0

"""
# construct adjacency list of graph
a = vertice("a")
b = vertice("b")
c = vertice("c")
d = vertice("d")
e = vertice("e")
f = vertice("f")

u = edge("u")
u.length = 1
u.left_node = a
u.right_node = b

v = edge("v")
v.length = 5
v.left_node = a
v.right_node = d

w = edge("w")
w.length = 3
w.left_node = b
w.right_node = c

x = edge("x")
x.length = 9
x.left_node = b
x.right_node = e

y = edge("y")
y.length = 2
y.left_node = c
y.right_node = d

z = edge("z")
z.length = 4
z.left_node = c
z.right_node = f

m = edge("m")
m.length = 6
m.left_node = d
m.right_node = e

n = edge("n")
n.length = 8
n.left_node = e
n.right_node = f

l = edge("l")
l.length = 7
l.left_node = a
l.right_node = f

u_a = incident_edges()
u_a.actual_edge = u
v_a = incident_edges()
v_a.actual_edge = v
l_a = incident_edges()
l_a.actual_edge = l
a.incident_edges = u_a
u_a.next = v_a
v_a.next = l_a

u_b = incident_edges()
u_b.actual_edge = u
w_b = incident_edges()
w_b.actual_edge = w
x_b = incident_edges()
x_b.actual_edge = x
b.incident_edges = u_b
u_b.next = w_b
w_b.next = x_b

w_c = incident_edges()
w_c.actual_edge = w
y_c = incident_edges()
y_c.actual_edge = y
z_c = incident_edges()
z_c.actual_edge = z
c.incident_edges = w_c
w_c.next = y_c
y_c.next = z_c


v_d = incident_edges()
v_d.actual_edge = v
y_d = incident_edges()
y_d.actual_edge = y
m_d = incident_edges()
m_d.actual_edge = m
d.incident_edges = v_d
v_d.next = y_d
y_d.next = m_d


x_e = incident_edges()
x_e.actual_edge = x
m_e = incident_edges()
m_e.actual_edge = m
n_e = incident_edges()
n_e.actual_edge = n
e.incident_edges = x_e
x_e.next = m_e
m_e.next = n_e


l_f = incident_edges()
l_f.actual_edge = l
z_f = incident_edges()
z_f.actual_edge = z
n_f = incident_edges()
n_f.actual_edge = n
f.incident_edges = l_f
l_f.next = z_f
z_f.next = n_f



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



Dijkstra(d)

first = True
print("Shortest distance from b to d: {}".format(b.distance))
node = b
while (node != None):
    if not first:
        print(" <-- {}".format(node.name), end="")
    else:
        first = False
        print("{}".format(node.name), end="")
    node = node.parent
print()
    
