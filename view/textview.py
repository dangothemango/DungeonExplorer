
class TextView:
    """a view class for displaying maze objects as text in the console"""

    def show(self,maze):
        printString="+"+"---+"*maze.width+"\n"
        for y in range (maze.height):
            printString+="|"
            for x in range(maze.width):
                node = maze.nodes[x][y]
                if ("start" in node.attributes):
                    printString+=" S "
                elif ("end" in node.attributes):
                    printString+=" E "
                else:
                    printString+="   "
                printString+=" " if node.hasRightEdge() else "|"
            printString+="\n+"
            for x in range(maze.width):
                node = maze.nodes[x][y]
                printString+="   +" if node.hasBottomEdge() else "---+"
            printString+="\n"
        print(printString)

