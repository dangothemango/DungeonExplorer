class edge:
    """The Edge class for the graph maze A -> B
    endNode is the destination node,
    Attributes[] is special features of this edge"""

    def __init__(self,endNode):
        self.attributes = []
        self.endNode = endNode

    def addAttribute(self,att):
        self.attributes.append(att)

class node:
    """A graph maze node designed to hold:
    references to its edges
    special attributes
    coordinates"""

    def __init__(self, x,y):
        self.edges = []
        self.attributes = []
        self.x = x
        self.y = y
        self.distance=0;

    def addEdge(self,m):
        if (self.isAdjacent(m)):
            self.edges.append(edge(m))

    def addAttribute(self,att):
        self.attributes.append(att)

    def isAdjacent(self, m):
        return abs(m.x-self.x) + abs(m.y-self.y) == 1

    def setDistance(self,dist):
        self.distance=dist

    def __str__(self):
        return "x: " +str(self.x) + " y: " +str(self.y)

    def __eq__(self, m):
        return (self.x == m.x and self.y == m.y)

        
if __name__ == "__main__":
    n = node(3,4)
    m = node(4,4)
    o = node(4,5)
    print('n:',n,'\nm:',m,'\no:',o)
    m.addEdge(m)
    m.addEdge(n)
    m.addEdge(o)
    for edge in m.edges:
        print(edge.endNode)