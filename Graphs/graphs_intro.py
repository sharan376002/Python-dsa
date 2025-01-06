# graphs 

class graphs:
    def __init__(self):
        self.graph = {}

   # adding the vertex like adding them  
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

    # remove the vertex
    def removeVertex(self,vertex):

        if vertex in self.graph:
            del self.graph[vertex]       
            
        for key,value in self.graph.items():
            if vertex in value:
                value.remove(vertex)  

    # depth first search
    def dfs_travsal(self,start,alreadyexist=set()):
        if start not in alreadyexist:
            alreadyexist.add(start)
            print(start,end=" ")


        for child in self.graph[start]:
            self.dfs_travsal(child, alreadyexist)
    
    # breadth first search
    def bfs_travsal(self,start):
        alreadyexist = {start}
        queue = []

        while len(queue)>0:
            current = queue.pop(0)
            print(current,end="")


            for child in self.graph[current]:
                if child not in alreadyexist:
                    queue.append(child)
                    alreadyexist.add(child)


    # Shortest Path
    def ShortestPath_bfs(self,start,end):
        alreadyexist = {start}
        queue = [(start,[start])]   


        while len(queue)>0:
            current,path = queue.pop(0)
            print(current,end="")


            for child in self.graph[current]:
                if child == end:
                    return path + [child]
                if child not in alreadyexist:
                    queue.append((child,path + [child]))
                    alreadyexist.add(child)             



v1 = graphs()
v1.addedges("A","B")
v1.addedges("B","C")
v1.addedges("C","D")
v1.addedges("B","D")


v1.dfs_travsal("A")
v1.dfs_travsal("B")
v1.dfs_travsal("C")
v1.dfs_travsal("D")
v1.dfs_travsal("B")
v1.dfs_travsal("B")




