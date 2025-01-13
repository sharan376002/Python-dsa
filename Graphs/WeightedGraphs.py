# the weight are value between the vertex
# like the distance between the value of two cities ex.. chennai to banglore distance is 300 , the 300 is weight

#weighteed graph

class WeightedGraph:
    def __init__(self):  # starting of the graph
        self.graph = {}

    def addVertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}    
        else:
            print("the vertex already exist")


    def addEdges(self,from_vertex,to_vertex,weight,isdirected=False):
        if from_vertex not in self.graph:
            self.addVertex(from_vertex)
        if to_vertex not in self.graph:    
            self.addVertex(to_vertex)

        
        self.graph[from_vertex][to_vertex] = weight

        if not isdirected:
            self.graph[to_vertex][from_vertex] = weight


    def RemoveEdges(self,from_vertex,to_vertex):

        if from_vertex in self.graph and to_vertex in self.graph[from_vertex]:
            del self.graph[from_vertex][to_vertex]

        if to_vertex in self.graph and from_vertex in self.graph[to_vertex]:
            del self.graph[to_vertex][from_vertex]



    def removeVertex(self,vertexs):
        if vertexs in self.graph:
            del self.graph[vertexs]

        for vertexIn in self.graph:
            if vertexs in self.graph[vertexIn]:
                del self.graph[vertexIn][vertexs]                


    def display(self):
        # Display the graph
        for vertex, edges in self.graph.items():
            print(f"{vertex} -> {edges}")




g1 = WeightedGraph()
g1.addEdges("C", "B", 300)
g1.addEdges("C", "D", 1300)
g1.addEdges("C", "M", 800)
g1.addEdges("M", "D", 700)

g1.display()
