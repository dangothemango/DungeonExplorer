import random
from maze.Components import node,edge

class maze:
    """The actual maze object. contains a list of nodes and functions for generation"""

    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.nodes=[]
        self.startNode = self.endNode = node(-1, -1)

        for x in range (width):
            column = []
            for y in range (height):
                column.append(node(x,y))
            self.nodes.append(column)

        self.setStartEnd()

        print(self.startNode)
        print(self.endNode, end="\n\n")

        self.generatePaths()
        self.generateAttributes()

    def setStartEnd(self):
        self.startNode = self.nodes[random.randint(0,self.width-1)][random.randint(0,self.height-1)]
        self.startNode.addAttribute('start')
        self.endNode = self.nodes[random.randint(0, self.width - 1)][random.randint(0, self.height - 1)]
        while self.endNode == self.startNode:
            self.endNode = self.nodes[random.randint(0,self.width-1)][random.randint(0,self.height-1)]
        self.endNode.addAttribute('end')

    def generatePaths(self):
        queue = [self.startNode,self.endNode]
        visited = [self.startNode,self.endNode]
        while len(queue)>0:
            n = queue.pop(0)
            print (n)
            for i in range (4):
                m = self.getRandomAdjacent(n)
                if (not visited.__contains__(m)):
                    visited.append(m)
                    n.addEdge(m)
                    m.addEdge(n)
                    m.setDistance(n.distance+1)
                    queue.insert(0,m)
            if len(queue) == 0:
                break
            n = queue.pop()
            print (n)
            for i in range (4):
                m = self.getRandomAdjacent(n)
                if (not visited.__contains__(m)):
                    visited.append(m)
                    n.addEdge(m)
                    m.addEdge(n)
                    m.setDistance(n.distance+1)
                    queue.append(m)

        for column in self.nodes:
            for node in column:
                print(node, end="-----")
                for edge in node.edges:
                    print("(", edge.endNode.x, ",", edge.endNode.y, ")", end=":")
                print()

    def getRandomAdjacent(self,n):
        direction = random.randint(0, 3)
        newNodeCoords = (
        (direction % 2) * (-1 if direction < 2 else 1), ((direction + 1) % 2) * (-1 if direction < 2 else 1))
        newNodeCoords = (min(max(newNodeCoords[0] + n.x, 0), self.width - 1),
                         min(max(newNodeCoords[1] + n.y, 0), self.height - 1))
        return self.nodes[newNodeCoords[0]][newNodeCoords[1]]

    def generateAttributes(self):
        return

if __name__=='__main__':
    m = maze(10,10)