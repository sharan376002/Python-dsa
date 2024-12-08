# qrrary are collectionof same data types
# static fixed memory

# arrays operations
'''
1. accesing element in array o(1)
2. insert element in array  o(1) , o(n-1)
3. delete  o(1) o(n-1) 
4. search   bestcase: o(1) , worstcase: 0(n)
'''

# accesing 
arr = [1,2,3,4,5,6,7]

print(arr[3])

# insert

ins = arr.insert(0,5)
print(arr)

#delete

dele = arr.remove(7)  # we can use also pop function
print(arr)

# search 

x=3
for i in range(0,len(arr)):
    if arr[i] == x:
        print(i)
        break
