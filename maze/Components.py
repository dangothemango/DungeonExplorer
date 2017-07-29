class Edge:
    """The Edge class for the graph maze A -> B
    endNode is the destination node,
    Attributes[] is special features of this edge"""

    def __init__(self,endNode):
        self.attributes = []
        self.endNode = endNode

    def addAttribute(self,att):
        self.attributes.append(att)

class Node:
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
            self.edges.append(Edge(m))

    def addAttribute(self,att):
        self.attributes.append(att)

    def isAdjacent(self, m):
        return abs(m.x-self.x) + abs(m.y-self.y) == 1

    def setDistance(self,dist):
        self.distance=dist

    def hasRightEdge(self):
        for edge in self.edges:
            if edge.endNode.x == self.x + 1 and edge.endNode.y == self.y:
                return True
        return False

    def hasBottomEdge(self):
        for edge in self.edges:
            if edge.endNode.x == self.x and edge.endNode.y == self.y+1:
                return True
        return False

    def __str__(self):
        return "x: " +str(self.x) + " y: " +str(self.y)

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)

    def __lt__(self, other):
        return self.distance<other.distance

    def __gt__(self, other):
        return self.distance>other.distance
        
if __name__ == "__main__":
    n = Node(3,4)
    m = Node(4,4)
    o = Node(4,5)
    print('n:',n,'\nm:',m,'\no:',o)
    m.addEdge(m)
    m.addEdge(n)
    m.addEdge(o)
    for edge in m.edges:
        print(edge.endNode)