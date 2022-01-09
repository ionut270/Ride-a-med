from collections import deque
ROW=21
COL=21
from ExtractData import ExtractData
class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"P({self.x},{self.y})"

class queueNode:
    def __init__(self, pt: Point, dist: int, parent=None):
        self.pt = pt  # The coordinates of the cell
        self.dist = dist  # Cell's distance from the source
        self.parent=parent
    def __str__(self):
        return f"{self.pt}:{self.dist}"
    def __repr__(self):
        return str(self)
# Check whether given cell(row,col)
# is a valid cell or not
def isValid(row: int, col: int):
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)

def getPath(node, path=[]):
    if node:
        getPath(node.parent, path)
        path.append(node)
    return path
# These arrays are used to get row and column
# numbers of 4 neighbours of a given cell
rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]


# Function to find the shortest path between
# a given source cell to a destination cell.
def BFS(mat, src: Point, dest: Point):
    # check source and destination cell
    # of the matrix have value 1
    # if mat[src.x][src.y] != 1 or mat[dest.x][dest.y] != 1:
    #     return -1

    visited = [[False for i in range(COL)]
               for j in range(ROW)]

    # Mark the source cell as visited
    visited[src.x][src.y] = True

    # Create a queue for BFS
    q = deque()

    # Distance of source cell is 0
    s = queueNode(src, 0)
    q.append(s)  # Enqueue source cell
    path=[]
    # Do a BFS starting from source cell
    while q:

        curr = q.popleft()  # Dequeue the front cell

        # If we have reached the destination cell,
        # we are done
        pt = curr.pt
        if pt.x == dest.x and pt.y == dest.y:
            path = []
            path=getPath(curr, path)
            return curr.dist,path

        # Otherwise enqueue its adjacent cells
        for i in range(4):
            row = pt.x + rowNum[i]
            col = pt.y + colNum[i]

            # if adjacent cell is valid, has path
            # and not visited yet, enqueue it.
            if (isValid(row, col) and not visited[row][col]):
                visited[row][col] = True
                Adjcell = queueNode(Point(row, col),mat[curr.pt.x][curr.pt.y]+curr.dist,curr)
                q.append(Adjcell)
                path.append(Adjcell)
    # Return -1 if destination cannot be reache
    return -1

extractData = ExtractData("E:\\anul III\\AI\\date_proiect\\easy\PTP-RAND-1_4_2_16.json")
matrix=extractData.getDistanceMatrix()
print(len(matrix),len(matrix[0]))
source = Point(4, 20)
dest = Point(2, 2)
dist = BFS(matrix, source, dest)

if dist != -1:
    print("Shortest Path is", dist)
else:
    print("Shortest Path doesn't exist")