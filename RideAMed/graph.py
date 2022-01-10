from Location import Location
from ExtractData import ExtractData
from PTP import PTP
from queue import PriorityQueue
class Node:
    def __init__(self,location:Location):
        self.id=location.getId()
        self.location=location

    def getNodeId(self):
        return self.id
    def __str__(self):
        return f"({self.id})"
    def __repr__(self):
        return str(self)
class Edge:
    def __init__(self,first_node,second_node,cost):
        self.first_node=first_node
        self.second_node=second_node
        self.cost=cost
    def getCost(self):
        return self.cost
    def getFirstNode(self):
        return self.first_node
    def getSecondNode(self):
        return self.second_node
    def __str__(self):
        return f"({self.first_node},{self.second_node},{self.cost})"
    def __repr__(self):
        return str(self)
class Graph:
    def __init__(self,nodes_list,edges_list):
        self.nodes_list=nodes_list
        self.edges_list=edges_list
    def getEdgeCost(self,nodex,nodey):
        if nodex>nodey:
            nodex,nodey=nodey,nodex
        for edge in self.edges_list:
            if edge.getFirstNode()==nodex and edge.getSecondNode()==nodey:
                return edge.cost
    def dijkstra(self,start_vertex:int):
            D = {v: float('inf') for v in range(len(self.nodes_list))}
            D[start_vertex] = 0
            visited=[]
            pq = PriorityQueue()
            pq.put((0, start_vertex))
            while not pq.empty():
                (dist, current_vertex) = pq.get()
                # print(current_vertex)
                visited.append(current_vertex)
                for neighbor in range(len(self.nodes_list)):
                    if self.getEdgeCost(current_vertex,neighbor) !=0 and current_vertex!=neighbor:
                        distance =self.getEdgeCost(current_vertex,neighbor)
                        # print(f"{current_vertex}->{neighbor} distance is: ",distance)
                        if neighbor not in visited:
                            old_cost = D[neighbor]
                            new_cost = D[current_vertex] + distance
                            if new_cost < old_cost:
                                pq.put((new_cost, neighbor))
                                D[neighbor] = new_cost
            return D

# extractData = ExtractData("E:\\anul III\\AI\\date_proiect\\easy\PTP-RAND-1_4_2_16.json")
# problem_instance = PTP(extractData.getMaxWaitTime(), extractData.getPatients(), extractData.getLocations(),extractData.getVehicles())
# matrix=extractData.getDistanceMatrix()
# k=0
# nodes_list=[]
# edges_list=[]
# for location in problem_instance.getLocations():
#     nodes_list.append(Node(location))
# for i in range(0,len(matrix)):
#     for j in range(i+1,len(matrix[0])):
#         edges_list.append(Edge(i,j,matrix[i][j]))
# print(edges_list)
# g=Graph(nodes_list,edges_list)
# print(g.dijkstra(4))
