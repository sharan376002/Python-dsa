class HashMap(dict):
    def __init__(self,size=10):
        
        self.size = size
        self.hashlist = [None]*self.size

    def getIndex(self,key):
        return hash(key) % self.size  
    def __setitem__(self,key,value):
        index = self.getIndex(key)

        if self.hashlist[index] is None:
            self.hashlist[index] = [[key,value]]
        else:
            self.hashlist[index].append([key,value])

    def __getitem__(self, key):
        index = self.getIndex(key)
        if self.hashlist[index]:
            sublist = self.hashlist[index]
            for pairs in sublist:
                if pairs[0]==key:
                    return pairs[1]
            return "key not found"    

    def __delitem__(self, key):
        index = self.getIndex(key)
        if self.hashlist[index]:
            sublist = self.hashlist[index]
            for i , pairs in enumerate(sublist):
                if pairs[0] == key:
                    del sublist[i]
                    return
            
        return 'key not found'    




 





