# the weight are value between the vertex
# like the distance between the value of two cities ex.. chennai to banglore distance is 300 , the 300 is weight

#weighteed graph

class WeightedGraph:
    def __init__(self):  # starting of the graph
        self.graph = {}

    def addVertex(self,vertex):
        if vertex not in self.graph:
            self.graph = {}    
        else:
            print("the vertex already exist")
    def addEdges(self,from_vertex,to_vertex,weight,isdirected=False):
        self.addVertex(from_vertex)
        self.addVertex(to_vertex)


        self.graph[from_vertex][to_vertex] = weight

        if isdirected == False:
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


