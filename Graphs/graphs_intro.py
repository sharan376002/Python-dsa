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
