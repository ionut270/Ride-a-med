from collections import defaultdict
ROW=21
COL=21
from ExtractData import ExtractData
from queue import PriorityQueue
class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight
def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D
if __name__ == '__main__':
    extractData = ExtractData("E:\\anul III\\AI\\date_proiect\\easy\PTP-RAND-1_4_2_16.json")
    matrix=extractData.getDistanceMatrix()
    k=0
    g=Graph(21)
    for i in range(0,len(matrix)):
        for j in range(i+1,len(matrix[0])):
            g.add_edge(i,j,matrix[i][j])
    D = dijkstra(g, 20)
    print(D)
    # print ("\nShortest Distance between %d and %d is %d " %(src, dest, l)),