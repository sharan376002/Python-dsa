arr = [1,2,3,4,5]
k = 4
x = 3

l=0
r=len(arr)-k

while l<r:

    mid = (l+r)//2

    if x-arr[mid] > arr[mid+k]-x:
        l= mid+1

    else:
        r=mid

print(arr[l:l+k])