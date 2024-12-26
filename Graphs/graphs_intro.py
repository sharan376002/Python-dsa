# graphs 

class graphs:
    def __init__(self):
        self.graph = {}
    
    def addvertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

        else:
            print("the vertex is already exist")    

    def addedges(self,vertex1,vertex2,_isdirected=False):
        self.addvertex(vertex1)
        self.addvertex(vertex2)
        self.graph[vertex1].append(vertex2)
        if not _isdirected:
            self.graph[vertex2].append(vertex1)

    def display(self):
        for key,value in self.graph.items():
            print(f"{key},{value}")    

    def getVertex(self):
        for i in self.graph:
            print(i) 

    def getedges(self):
        for key,value in self.graph.items():
            for vetex in value:
                print(f"{(key)},{(value)}")      

    def removeVertex(self,vertex):

        if vertex in self.graph:
            del self.graph[vertex]       
            
        for key,value in self.graph.items():
            if vertex in value:
                value.remove(vertex)             


