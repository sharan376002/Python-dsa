# same direction (sliding window )
# opposite direction

# choose two pointer from two differnt direction 
# l and r 

# the array must be sorted 


# time complexity in using of two poin=ter algorithm  - o(n)
# In the normal way the time complexity is o(n^2)

#TWo sums probles

arr = [1,2,3,4,5,6]

target = 11
l = 0
r= len(arr)-1
while (l<r):
    actual_value = arr[l]+ arr[r]
    if actual_value == target:
        print(l,r)
        break
    elif actual_value <target:
        l = l+1
    elif actual_value>target:
        r = r+1    