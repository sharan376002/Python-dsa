# the weight are value between the vertex
# like the distance between the value of two cities ex.. chennai to banglore distance is 300 , the 300 is weight

#weighteed graph

class WeightedGraph:
    def __init__(self):
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