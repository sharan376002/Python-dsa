# graphs 

class graphs:
    def __init__(self):
        self.graph = {}
    
    def addvertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

        else:
            print("the vertex is already exist")    