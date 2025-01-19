class HashMap:
    def __init__(self,size=10):
        
        self.size = size
        self.hashlist = [None]*self.size

    def getIndex(self,key):
        return hash(key) % self.size  

    def __setitem__(self,key,value):
        index = self.getIndex(key)

        if self.hashlist[index] is None:
            self.hashlist[index] = [[key,value]]





            