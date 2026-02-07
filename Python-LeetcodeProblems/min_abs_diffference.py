arr = [4,2,1,3]


rs = []
l = 1

arr.sort()

for i in range(len(arr)):
    nxt = arr[i] + 1
    if l<len(arr) and nxt == arr[l]:
        rs.append([arr[i],arr[l]])
    l+=1
    
        
    

print(rs)

"""

class Solution(object):
    def minimumAbsDifference(self, arr):

        rs = []
        l = 1

        arr.sort()

        # find minimum difference first
        min_diff = float("inf")
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]s
            if diff < min_diff:
                min_diff = diff

        # collect pairs with that minimum difference
        for i in range(len(arr)):
            if l < len(arr) and arr[l] - arr[i] == min_diff:
                rs.append([arr[i], arr[l]])
            l += 1

        return rs



"""
