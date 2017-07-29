import random
from maze.Components import Node

class Maze:
    """The actual maze object. contains a list of nodes and functions for generation"""

    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.nodes=[]
        self.startNode = self.endNode = Node(-1, -1)

        for x in range (width):
            column = []
            for y in range (height):
                column.append(Node(x,y))
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
        collisions = []
        while len(queue)>0:
            n = queue.pop(0)
            for i in range (4):
                m = self.getRandomAdjacent(n)
                if (m not in visited):
                    visited.append(m)
                    n.addEdge(m)
                    m.addEdge(n)
                    m.setDistance(n.distance+1)
                    queue.insert(0,m)
                elif m.distance<0:
                    collisions.append((n,m))

            if len(queue) == 0:
                break
            n = queue.pop()
            for i in range (4):
                m = self.getRandomAdjacent(n)
                if (m not in visited):
                    visited.append(m)
                    n.addEdge(m)
                    m.addEdge(n)
                    m.setDistance(n.distance-1)
                    queue.append(m)
                elif m.distance > 0:
                    collisions.append((n, m))
        maxCollision=(Node(-1,-1),Node(-1,-1),-1)
        while len(collisions)>0:
            collision = collisions.pop()
            if abs(collision[0].distance)+abs(collision[1].distance)>maxCollision[2]:
                maxCollision = (collision[0],collision[1],abs(collision[0].distance)+abs(collision[1].distance))
        if (maxCollision[0] != Node(-1,-1) and maxCollision[1] != Node(-1,-1)):
            maxCollision[0].addEdge(maxCollision[1])
            maxCollision[1].addEdge(maxCollision[0])
        else:
            self.generatePaths()


    def getRandomAdjacent(self,n):
        direction = random.randint(0, 3)
        newNodeCoords = ((direction % 2) * (-1 if direction < 2 else 1), ((direction + 1) % 2) * (-1 if direction < 2 else 1))
        newNodeCoords = (min(max(newNodeCoords[0] + n.x, 0), self.width - 1),
                         min(max(newNodeCoords[1] + n.y, 0), self.height - 1))
        return self.nodes[newNodeCoords[0]][newNodeCoords[1]]

    def generateAttributes(self):
        return

if __name__=='__main__':
    maze = Maze(10,10)